# 3D Print Profile Retrieval
Retrieve 3D Printer profiles from gCode

Accidentally erased a profile from Simplify3D, was kicking myself until I realised I still had a gCode file lying around that used said profile. Wrote this to convert the S3D gCode comments into a usable profile.

## What It's Capable Of
**This can currently only open gCode files generated by Simplfy3D**

Supported Slicers:
   * Simplify3D :✅
   * Cura:       ❌ (Probably in the future)

Pulls out all settings for:
   * Extruder   ✅ (However, only supports primary extruder)
   * Layer      ✅
   * Additions  ✅
   * Infill     ✅
   * Support    ✅
   * Temperature❌ (next on todo list)
   * Cooling    ❌ (next on todo list)
   * Scripts    ❌ (currently a bug)
   * Speeds     ✅
   * Other      ✅
   * Advanced   ✅ 
   
## How to use
Have python 3 installed

1. Open a command line
2. Enter: python directoryPath/3dretrieve.py
3. Drag the gCode you want to extract settings from into the command window
4. Type out the name you want to give the retrieved profile
5. Done!

## Troubleshooting
This script relies on Simplify3D automatically adding the profile settings to the top of the gCode file. If you open your desired gCode file in a notepad app, it should have the top three lines, followed by lots of commented settings:

; G-Code generated by Simplify3D(R) Version 4.1.2

; Apr 21, 2020 at 6:47:40 PM

; Settings Summary


I have only tested this with Simplify3D 4.1.2, but it should be backwards compatible... I just don't know how far
