// 0. Go to "Corpse Party RF/CorpseParty_Data/Managed/" and make a backup of this file: Assembly-CSharp.dll, just copy it somewhere
// 1. Open dnSpy.exe
// 2. In dnSpy, open "Corpse Party RF/CorpseParty_Data/Managed/Assembly-CSharp.dll"
// 3. Open the following path in the left side window:
// Assembly-CSharp (0.0.0.0)
//   Assembly-CSharp.dll
// 	   {} -
// 	     TalkWindowControl
// 4. In the left side window, below TalkWindowControl, right click on "SetMessage" and select "Edit Method C#". A new window should open
// 5. In the new window, paste the following text below line 15:
if (!(this.voicelist_txt == null) && this.voicelist_txt.commonStringData != null && this.voicelist_txt.commonStringData.Count != 0 && this.m_Control.VoiceNumber > 0 && this.voicelist_txt.commonStringData.Count >= this.m_Control.VoiceNumber && this.voicelist_txt.commonStringData[this.m_Control.VoiceNumber] != null && this.voicelist_txt.commonStringData[this.m_Control.VoiceNumber].Data != null) {
	GUIUtility.systemCopyBuffer = "[Sound:" + this.voicelist_txt.commonStringData[this.m_Control.VoiceNumber].Data + "]" + this.m_Control.Message;
    return;
}
GUIUtility.systemCopyBuffer = this.m_Control.Message;
// Note:  The only thing after the text you pasted should be these two symbols: } }
// 6. At the bottom of the window, click "Compile". The window should close automatically. If it doesn't then you did something wrong. Read the red error message and try again.
// 7. In dnSpy, click File -> Save Module. A new small window should open.
// 8. Click "Ok"
// 9. Done
//
// In case your game crashes or you just want to restore the game how it was originally, just replace Corpse Party RF/CorpseParty_Data/Managed/Assembly-CSharp.dll with the file you backed up in step 0.
