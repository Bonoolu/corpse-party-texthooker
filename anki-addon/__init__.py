import time
import re
from aqt.qt import os, QGuiApplication, QAction, qconnect
from aqt.operations import QueryOp
from aqt import mw
import aqt
import signal


def start_clipboard_loop() -> None:
    op = QueryOp(op=clipboard_loop, success=lambda: None, parent=mw)
    op.run_in_background()


def clipboard_loop(_):
    global audio_filename
    prev_clipboard_text_stripped = ""
    while True:
        try:
            clipboard_text_orig = clipboard.text()
            result = pattern_sound.findall(clipboard_text_orig)
            if result:
                audio_filename = result[0]
                clipboard_text_stripped = pattern_sound.sub("", clipboard_text_orig)
                clipboard.setText(clipboard_text_stripped)
            else:
                clipboard_text_stripped = clipboard_text_orig
            if clipboard_text_stripped and clipboard_text_stripped != prev_clipboard_text_stripped:
                if not result:
                    audio_filename = ""
                prev_clipboard_text_stripped = clipboard_text_stripped
                if audio_filename:
                    print(f"[sound:{audio_filename}.opus]", clipboard_text_stripped)
                else:
                    print(clipboard_text_stripped)
        except Exception as e:
            print("Error:", e)
        time.sleep(0.3)
        if not mw.isVisible():
            return


def get_last_note_id():
    highest_nid = 0
    for note in mw.col.find_notes('added:1'):
        if note > highest_nid:
            highest_nid = note
    return highest_nid


def make_screenshot():
    with os.popen('corpse-screenshot.sh', 'r') as screenshot:
        return screenshot.read().replace("\n", "")


def add_audio_to_most_recent_node(_, __):
    nid = get_last_note_id()
    if not nid:
        return
    note = mw.col.get_note(nid)
    if audio_filename:
        audio_dir = '/home/admin/Development/IdeaProjects/python/corpse-party-texthooker/sound/'
        audio_path = f'{audio_dir}{audio_filename}.opus'
        mw.col.media.add_file(audio_path)
        note["SentAudio"] = f'[sound:{audio_filename}.opus]'
    note.tags.append('corpse')
    note.tags.append('visual-novel')
    screenshot_path = make_screenshot()
    screenshot_filename = screenshot_path.replace("/tmp/", "")
    mw.col.media.add_file(screenshot_path)
    note["Image"] = f'<img alt="snapshot" src="{screenshot_filename}">'
    mw.col.update_note(note)
    browser = aqt.dialogs.open('Browser', mw.window())
    browser.activateWindow()
    browser.form.searchEdit.lineEdit().setText(f'nid:{int(nid)}')
    if hasattr(browser, 'onSearch'):
        browser.onSearch()
    else:
        browser.onSearchActivated()


signal.signal(signal.SIGUSR1, add_audio_to_most_recent_node)
audio_filename = ""
pattern_sound = re.compile(r'\[Sound:(.*)]', flags=re.IGNORECASE)
clipboard = QGuiApplication.clipboard()
action = QAction("Start corpse party addon", mw)
qconnect(action.triggered, start_clipboard_loop)
mw.form.menuTools.addAction(action)
