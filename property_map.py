"""
Sony Camera PTP-IP Property Code Mapping
Auto-generated from tblDevicePropertyCodeList in libCr_Core.so
Binary: libCr_Core.so SHA256:727730a8...

CrSDK internal codes (0x01xx-0x09xx) <-> PTP wire codes (0x50xx + 0xD0xx-0xF0xx)
810 entries from the binary lookup table, names from CrDeviceProperty.h
"""


CRSDK_TO_WIRE = {
    0x0100: 0x5007,  # FNumber
    0x0101: 0x5010,  # ExposureBiasCompensation
    0x0102: 0xD200,  # FlashCompensation
    0x0103: 0xD20D,  # ShutterSpeed
    0x0104: 0xD21E,  # IsoSensitivity
    0x0105: 0x500E,  # ExposureProgramMode
    0x0106: 0xD253,  # FileType
    0x012B: 0xD28B,  # MediaSLOT1_FileType
    0x012C: 0xD28C,  # MediaSLOT2_FileType
    0x0107: 0xD252,  # StillImageQuality
    0x012D: 0xD28D,  # MediaSLOT1_ImageQuality
    0x012E: 0xD28E,  # MediaSLOT2_ImageQuality
    0x0108: 0x5005,  # WhiteBalance
    0x0109: 0x500A,  # FocusMode
    0x010A: 0x500B,  # MeteringMode
    0x010B: 0x500C,  # FlashMode
    0x010C: 0xD262,  # WirelessFlash
    0x010D: 0xD263,  # RedEyeReduction
    0x010E: 0x5013,  # DriveMode
    0x010F: 0xD201,  # DRO
    0x0110: 0xD203,  # ImageSize
    0x012F: 0xD28F,  # MediaSLOT1_ImageSize
    0x0130: 0xD290,  # MediaSLOT2_ImageSize
    0x0111: 0xD211,  # AspectRatio
    0x0112: 0xD21B,  # PictureEffect
    0x0113: 0xD22C,  # FocusArea
    0x0114: 0xD219,  # reserved4
    0x0115: 0xD20F,  # Colortemp
    0x0116: 0xD21C,  # ColorTuningAB
    0x0117: 0xD210,  # ColorTuningGM
    0x0118: 0xD231,  # LiveViewDisplayEffect
    0x0119: 0xD222,  # StillImageStoreDestination
    0x011A: 0xD25A,  # PriorityKeySettings
    0x011B: 0xD255,  # AFTrackingSensitivity
    0x011D: 0xD254,  # Focus_Magnifier_Setting
    0x011E: 0xD223,  # DateTime_Settings
    0x0124: 0xD25C,  # Zoom_Scale
    0x0125: 0xD25F,  # Zoom_Setting
    0x0127: 0xD241,  # Movie_File_Format
    0x0128: 0xD242,  # Movie_Recording_Setting
    0x0129: 0xD286,  # Movie_Recording_FrameRateSetting
    0x012A: 0xD287,  # CompressionFileFormatStill
    0x0131: 0xD288,  # RAW_FileCompressionType
    0x0132: 0xD289,  # MediaSLOT1_RAW_FileCompressionType
    0x0133: 0xD28A,  # MediaSLOT2_RAW_FileCompressionType
    0x0136: 0xD001,  # IrisModeSetting
    0x0137: 0xD013,  # ShutterModeSetting
    0x0138: 0xD01C,  # GainControlSetting
    0x0139: 0xD020,  # GainBaseIsoSensitivity
    0x013A: 0xD021,  # GainBaseSensitivity
    0x013B: 0xD022,  # ExposureIndex
    0x013C: 0xD03C,  # BaseLookValue
    0x013D: 0xD042,  # PlaybackMedia
    0x013E: 0xD045,  # DispModeSetting
    0x013F: 0xD046,  # DispMode
    0x0140: 0xD047,  # TouchOperation
    0x0141: 0xD048,  # SelectFinderMonitor
    0x0142: 0xD049,  # AutoPowerOffTemperature
    0x0143: 0xD04A,  # BodyKeyLock
    0x0144: 0xD092,  # ImageID_Num_Setting
    0x0145: 0xD04B,  # ImageID_Num
    0x0146: 0xD04C,  # ImageID_String
    0x0147: 0xD099,  # ExposureCtrlType
    0x0148: 0xD04D,  # MonitorLUTSetting
    0x0149: 0xD004,  # FocalDistanceInMeter
    0x014A: 0xD005,  # FocalDistanceInFeet
    0x014B: 0xD006,  # FocalDistanceUnitSetting
    0x014C: 0xD00A,  # DigitalZoomScale
    0x014D: 0xD00B,  # ZoomDistance
    0x014E: 0xD029,  # ZoomDistanceUnitSetting
    0x014F: 0xD011,  # ShutterModeStatus
    0x0150: 0xD014,  # ShutterSlow
    0x0151: 0xD015,  # ShutterSlowFrames
    0x0152: 0xD024,  # Movie_Recording_ResolutionForMain
    0x0153: 0xD025,  # Movie_Recording_ResolutionForProxy
    0x0154: 0xD028,  # Movie_Recording_FrameRateProxySetting
    0x0155: 0xD037,  # BatteryRemainDisplayUnit
    0x0156: 0xD03A,  # PowerSource
    0x0157: 0xE000,  # MovieShootingMode
    0x0158: 0xE001,  # MovieShootingModeColorGamut
    0x0159: 0xE002,  # MovieShootingModeTargetDisplay
    0x015A: 0xE009,  # DepthOfFieldAdjustmentMode
    0x015C: 0xD00C,  # WhiteBalanceModeSetting
    0x015D: 0xD00D,  # WhiteBalanceTint
    0x0160: 0xE006,  # ShutterECSSetting
    0x0161: 0xE007,  # ShutterECSNumber
    0x0163: 0xE008,  # ShutterECSFrequency
    0x0164: 0xE00D,  # RecorderControlProxySetting
    0x0165: 0xE014,  # ButtonAssignmentAssignable1
    0x0166: 0xE015,  # ButtonAssignmentAssignable2
    0x0167: 0xE016,  # ButtonAssignmentAssignable3
    0x0168: 0xE017,  # ButtonAssignmentAssignable4
    0x0169: 0xE018,  # ButtonAssignmentAssignable5
    0x016A: 0xE019,  # ButtonAssignmentAssignable6
    0x016B: 0xE01A,  # ButtonAssignmentAssignable7
    0x016C: 0xE01B,  # ButtonAssignmentAssignable8
    0x016D: 0xE01C,  # ButtonAssignmentAssignable9
    0x021F: 0xE01D,  # ButtonAssignmentAssignable10
    0x0220: 0xE08D,  # ButtonAssignmentAssignable11
    0x016E: 0xE01E,  # ButtonAssignmentLensAssignable1
    0x016F: 0xE029,  # AssignableButton1
    0x0170: 0xE02A,  # AssignableButton2
    0x0171: 0xE02B,  # AssignableButton3
    0x0172: 0xE02C,  # AssignableButton4
    0x0173: 0xE02D,  # AssignableButton5
    0x0174: 0xE02E,  # AssignableButton6
    0x0175: 0xE02F,  # AssignableButton7
    0x0176: 0xE030,  # AssignableButton8
    0x0177: 0xE031,  # AssignableButton9
    0x0225: 0xE032,  # AssignableButton10
    0x0226: 0xE08E,  # AssignableButton11
    0x0178: 0xE033,  # LensAssignableButton1
    0x0179: 0xD007,  # FocusModeSetting
    0x017A: 0xD00E,  # ShutterAngle
    0x017B: 0xD00F,  # ShutterSetting
    0x017C: 0xD010,  # ShutterMode
    0x017D: 0xD016,  # ShutterSpeedValue
    0x017E: 0xD018,  # NDFilter
    0x017F: 0xD01A,  # NDFilterModeSetting
    0x0180: 0xD01B,  # NDFilterValue
    0x0181: 0xD01D,  # GainUnitSetting
    0x0182: 0xD01E,  # GaindBValue
    0x0183: 0xD03B,  # AWB
    0x0184: 0xE01F,  # SceneFileIndex
    0x0185: 0xE021,  # MoviePlayButton
    0x0186: 0xE022,  # MoviePlayPauseButton
    0x0187: 0xE023,  # MoviePlayStopButton
    0x0188: 0xE024,  # MovieForwardButton
    0x0189: 0xE025,  # MovieRewindButton
    0x018A: 0xE026,  # MovieNextButton
    0x018B: 0xE027,  # MoviePrevButton
    0x018C: 0xE028,  # MovieRecReviewButton
    0x018D: 0xD060,  # SubjectRecognitionAF
    0x018E: 0xD061,  # AFTransitionSpeed
    0x018F: 0xD062,  # AFSubjShiftSens
    0x0190: 0xE084,  # AFAssist
    0x0191: 0xD073,  # NDFilterSwitchingSetting
    0x0192: 0xE083,  # FunctionOfRemoteTouchOperation
    0x0194: 0xE088,  # FollowFocusPositionSetting
    0x0195: 0xD2A1,  # FocusBracketShotNumber
    0x0196: 0xD2A2,  # FocusBracketFocusRange
    0x0197: 0xD0C5,  # ExtendedInterfaceMode
    0x0198: 0xD0D0,  # SQRecordingFrameRateSetting
    0x0199: 0xD052,  # SQFrameRate
    0x019A: 0xD0D1,  # SQRecordingSetting
    0x019B: 0xD0D2,  # AudioRecording
    0x019C: 0xE050,  # AudioInputMasterLevel
    0x019D: 0xD0D3,  # TimeCodePreset
    0x019E: 0xD0D5,  # TimeCodeFormat
    0x019F: 0xD0D6,  # TimeCodeRun
    0x01A0: 0xD0D7,  # TimeCodeMake
    0x01A1: 0xD0D4,  # UserBitPreset
    0x01A2: 0xD0D8,  # UserBitTimeRec
    0x01A3: 0xD0D9,  # ImageStabilizationSteadyShot
    0x01A4: 0xD0DA,  # Movie_ImageStabilizationSteadyShot
    0x01A5: 0xD0DB,  # SilentMode
    0x01A6: 0xD0DC,  # SilentModeApertureDriveInAF
    0x01A7: 0xD0DD,  # SilentModeShutterWhenPowerOff
    0x01A8: 0xD0DE,  # SilentModeAutoPixelMapping
    0x01A9: 0xD0DF,  # ShutterType
    0x01AA: 0xD23F,  # PictureProfile
    0x01AB: 0xD0E0,  # PictureProfile_BlackLevel
    0x01AC: 0xD0E1,  # PictureProfile_Gamma
    0x01AD: 0xD0E2,  # PictureProfile_BlackGammaRange
    0x01AE: 0xD0E3,  # PictureProfile_BlackGammaLevel
    0x01AF: 0xD0E4,  # PictureProfile_KneeMode
    0x01B0: 0xD0E5,  # PictureProfile_KneeAutoSet_MaxPoint
    0x01B1: 0xD0E6,  # PictureProfile_KneeAutoSet_Sensitivity
    0x01B2: 0xD0E7,  # PictureProfile_KneeManualSet_Point
    0x01B3: 0xD0E8,  # PictureProfile_KneeManualSet_Slope
    0x01B4: 0xD0E9,  # PictureProfile_ColorMode
    0x01B5: 0xD0EA,  # PictureProfile_Saturation
    0x01B6: 0xD0EB,  # PictureProfile_ColorPhase
    0x01B7: 0xD0EC,  # PictureProfile_ColorDepthRed
    0x01B8: 0xD0ED,  # PictureProfile_ColorDepthGreen
    0x01B9: 0xD0EE,  # PictureProfile_ColorDepthBlue
    0x01BA: 0xD0EF,  # PictureProfile_ColorDepthCyan
    0x01BB: 0xD0F0,  # PictureProfile_ColorDepthMagenta
    0x01BC: 0xD0F1,  # PictureProfile_ColorDepthYellow
    0x01BD: 0xD0F2,  # PictureProfile_DetailLevel
    0x01BE: 0xD0F3,  # PictureProfile_DetailAdjustMode
    0x01BF: 0xD0F4,  # PictureProfile_DetailAdjustVHBalance
    0x01C0: 0xD0F5,  # PictureProfile_DetailAdjustBWBalance
    0x01C1: 0xD0F6,  # PictureProfile_DetailAdjustLimit
    0x01C2: 0xD0F7,  # PictureProfile_DetailAdjustCrispening
    0x01C3: 0xD0F8,  # PictureProfile_DetailAdjustHiLightDetail
    0x01C4: 0xD0F9,  # PictureProfile_Copy
    0x01C5: 0xD0FA,  # CreativeLook
    0x01C6: 0xD0FB,  # CreativeLook_Contrast
    0x01C7: 0xD0FC,  # CreativeLook_Highlights
    0x01C8: 0xD0FD,  # CreativeLook_Shadows
    0x01C9: 0xD0FE,  # CreativeLook_Fade
    0x01CA: 0xD0FF,  # CreativeLook_Saturation
    0x01CB: 0xD100,  # CreativeLook_Sharpness
    0x01CC: 0xD101,  # CreativeLook_SharpnessRange
    0x01CD: 0xD102,  # CreativeLook_Clarity
    0x01CE: 0xD103,  # CreativeLook_CustomLook
    0x01CF: 0xD027,  # Movie_ProxyFileFormat
    0x01D0: 0xD109,  # ProxyRecordingSetting
    0x01D1: 0xD283,  # FunctionOfTouchOperation
    0x01D2: 0xD281,  # HighResolutionShutterSpeedSetting
    0x01D3: 0xD0C7,  # DeleteUserBaseLook
    0x01D4: 0xD0C8,  # SelectUserBaseLookToEdit
    0x01D5: 0xD0CC,  # SelectUserBaseLookToSetInPPLUT
    0x01D6: 0xD0C9,  # UserBaseLookInput
    0x01D7: 0xD0CA,  # UserBaseLookAELevelOffset
    0x01D8: 0xD0CB,  # BaseISOSwitchEI
    0x01D9: 0xD133,  # FlickerLessShooting
    0x01DA: 0xD172,  # AudioLevelDisplay
    0x01DB: 0xD17C,  # PlaybackVolumeSettings
    0x01DC: 0xD17D,  # AutoReview
    0x01DD: 0xD17E,  # AudioSignals
    0x01DE: 0xD17F,  # HDMIResolutionStillPlay
    0x01DF: 0xD180,  # Movie_HDMIOutputRecMedia
    0x01E0: 0xD181,  # Movie_HDMIOutputResolution
    0x01E1: 0xD182,  # Movie_HDMIOutput4KSetting
    0x01E2: 0xD183,  # Movie_HDMIOutputRAW
    0x01E3: 0xD184,  # Movie_HDMIOutputRawSetting
    0x01E4: 0xD185,  # Movie_HDMIOutputColorGamutForRAWOut
    0x01E5: 0xD186,  # Movie_HDMIOutputTimeCode
    0x01E6: 0xD187,  # Movie_HDMIOutputRecControl
    0x01E8: 0xD079,  # MonitoringOutputDisplayHDMI
    0x01E9: 0xE059,  # Movie_HDMIOutputAudioCH
    0x01EA: 0xD055,  # Movie_IntervalRec_IntervalTime
    0x01EB: 0xD151,  # Movie_IntervalRec_FrameRateSetting
    0x01EC: 0xD152,  # Movie_IntervalRec_RecordingSetting
    0x01ED: 0xD0CD,  # EframingScaleAuto
    0x01EE: 0xD0CE,  # EframingSpeedAuto
    0x01EF: 0xD124,  # EframingModeAuto
    0x01F0: 0xD153,  # EframingRecordingImageCrop
    0x01F1: 0xD154,  # EframingHDMICrop
    0x01F2: 0xD0CF,  # CameraEframing
    0x01F3: 0xD150,  # USBPowerSupply
    0x01F4: 0xD15B,  # LongExposureNR
    0x01F5: 0xD15C,  # HighIsoNR
    0x01F6: 0xD15D,  # HLGStillImage
    0x01F7: 0xD15E,  # ColorSpace
    0x01F8: 0xD166,  # BracketOrder
    0x01F9: 0xD167,  # FocusBracketOrder
    0x01FA: 0xD168,  # FocusBracketExposureLock1stImg
    0x01FB: 0xD169,  # FocusBracketIntervalUntilNextShot
    0x01FC: 0xD16A,  # IntervalRec_ShootingStartTime
    0x01FD: 0xD16B,  # IntervalRec_ShootingInterval
    0x01FE: 0xD16F,  # IntervalRec_ShootIntervalPriority
    0x01FF: 0xD16C,  # IntervalRec_NumberOfShots
    0x0200: 0xD16D,  # IntervalRec_AETrackingSensitivity
    0x0201: 0xD16E,  # IntervalRec_ShutterType
    0x0202: 0xD170,  # ElectricFrontCurtainShutter
    0x0203: 0xD171,  # WindNoiseReduct
    0x0204: 0xD29C,  # RecordingSelfTimer
    0x0205: 0xD29D,  # RecordingSelfTimerCountTime
    0x0206: 0xD29F,  # RecordingSelfTimerContinuous
    0x0207: 0xD2A0,  # RecordingSelfTimerStatus
    0x0208: 0xD2A4,  # BulbTimerSetting
    0x0209: 0xD2A5,  # BulbExposureTimeSetting
    0x020A: 0xD173,  # AutoSlowShutter
    0x020B: 0xD14D,  # IsoAutoMinShutterSpeedMode
    0x020C: 0xD176,  # IsoAutoMinShutterSpeedManual
    0x020D: 0xD177,  # IsoAutoMinShutterSpeedPreset
    0x020E: 0xE042,  # FocusPositionSetting
    0x020F: 0xD178,  # SoftSkinEffect
    0x0210: 0xD179,  # PrioritySetInAF_S
    0x0211: 0xD17A,  # PrioritySetInAF_C
    0x0212: 0xD17B,  # FocusMagnificationTime
    0x0213: 0xD157,  # SubjectRecognitionInAF
    0x0214: 0xD158,  # RecognitionTarget
    0x0215: 0xD159,  # RightLeftEyeSelect
    0x0216: 0xD27C,  # SelectFTPServer
    0x0217: 0xD02E,  # SelectFTPServerID
    0x0218: 0xD041,  # FTP_Function
    0x0219: 0xD04E,  # FTP_AutoTransfer
    0x021A: 0xD04F,  # FTP_AutoTransferTarget
    0x021B: 0xD199,  # Movie_FTP_AutoTransferTarget
    0x021C: 0xD19A,  # FTP_TransferTarget
    0x021D: 0xD14B,  # Movie_FTP_TransferTarget
    0x021E: 0xD14C,  # FTP_PowerSave
    0x022B: 0xD14E,  # NDFilterUnitSetting
    0x022C: 0xD14F,  # NDFilterOpticalDensityValue
    0x022D: 0xD000,  # TNumber
    0x022E: 0xD003,  # IrisDisplayUnit
    0x022F: 0xE080,  # Movie_ImageStabilizationLevel
    0x0230: 0xD192,  # ImageStabilizationSteadyShotAdjust
    0x0231: 0xD193,  # ImageStabilizationSteadyShotFocalLength
    0x0232: 0xD19F,  # ExtendedShutterSpeed
    0x0233: 0xD208,  # CameraButtonFunction
    0x0234: 0xD209,  # CameraButtonFunctionMulti
    0x0235: 0xD20A,  # CameraDialFunction
    0x0236: 0xD155,  # SynchroterminalForcedOutput
    0x0237: 0xD156,  # ShutterReleaseTimeLagControl
    0x0238: 0xD12F,  # ContinuousShootingSpotBoostFrameSpeed
    0x0239: 0xD189,  # TimeShiftShooting
    0x023A: 0xD18A,  # TimeShiftTriggerSetting
    0x023B: 0xD18B,  # TimeShiftPreShootingTimeSetting
    0x023C: 0xD196,  # EmbedLUTFile
    0x023D: 0xD1C7,  # APS_C_S35
    0x023E: 0xD1A2,  # LensCompensationShading
    0x023F: 0xD1A3,  # LensCompensationChromaticAberration
    0x0240: 0xD1A4,  # LensCompensationDistortion
    0x0241: 0xD1A5,  # LensCompensationBreathing
    0x0242: 0xD15F,  # RecordingMedia
    0x0243: 0xD160,  # Movie_RecordingMedia
    0x0244: 0xD161,  # AutoSwitchMedia
    0x0245: 0xD1C8,  # RecordingFileNumber
    0x0246: 0xD2B5,  # Movie_RecordingFileNumber
    0x0247: 0xD1CA,  # RecordingSettingFileName
    0x0248: 0xD1CB,  # RecordingFolderFormat
    0x024A: 0xD132,  # SelectIPTCMetadata
    0x024B: 0xD1CD,  # WriteCopyrightInfo
    0x024C: 0xD1CE,  # SetPhotographer
    0x024D: 0xD1CF,  # SetCopyright
    0x024E: 0xD1DC,  # FileSettingsTitleNameSettings
    0x024F: 0xD1A6,  # FocusBracketRecordingFolder
    0x0250: 0xD1A7,  # ReleaseWithoutLens
    0x0251: 0xD1A8,  # ReleaseWithoutCard
    0x0252: 0xD1DE,  # GridLineDisplay
    0x0253: 0xD162,  # ContinuousShootingSpeedInElectricShutterHiPlus
    0x0254: 0xD163,  # ContinuousShootingSpeedInElectricShutterHi
    0x0255: 0xD164,  # ContinuousShootingSpeedInElectricShutterMid
    0x0256: 0xD165,  # ContinuousShootingSpeedInElectricShutterLo
    0x0257: 0xD1B6,  # IsoAutoRangeLimitMin
    0x0258: 0xD1B7,  # IsoAutoRangeLimitMax
    0x0259: 0xD1E5,  # FacePriorityInMultiMetering
    0x025A: 0xD1AA,  # PrioritySetInAWB
    0x025B: 0xD135,  # CustomWB_Size_Setting
    0x025C: 0xD1AB,  # AFIlluminator
    0x025D: 0xD1AC,  # ApertureDriveInAF
    0x025E: 0xD1AD,  # AFWithShutter
    0x025F: 0xD1AE,  # FullTimeDMF
    0x0260: 0xD1AF,  # PreAF
    0x0261: 0xD1E6,  # SubjectRecognitionPersonTrackingSubjectShiftRange
    0x0262: 0xD1E7,  # SubjectRecognitionAnimalBirdPriority
    0x0263: 0xD1E8,  # SubjectRecognitionAnimalBirdDetectionParts
    0x0264: 0xD1E9,  # SubjectRecognitionAnimalTrackingSubjectShiftRange
    0x0265: 0xD1EA,  # SubjectRecognitionAnimalTrackingSensitivity
    0x0266: 0xD1EB,  # SubjectRecognitionAnimalDetectionSensitivity
    0x0267: 0xD1EC,  # SubjectRecognitionAnimalDetectionParts
    0x0268: 0xD1ED,  # SubjectRecognitionBirdTrackingSubjectShiftRange
    0x0269: 0xD1EE,  # SubjectRecognitionBirdTrackingSensitivity
    0x026A: 0xD1EF,  # SubjectRecognitionBirdDetectionSensitivity
    0x026B: 0xD1F0,  # SubjectRecognitionBirdDetectionParts
    0x026C: 0xD1F1,  # SubjectRecognitionInsectTrackingSubjectShiftRange
    0x026D: 0xD1F2,  # SubjectRecognitionInsectTrackingSensitivity
    0x026E: 0xD1F3,  # SubjectRecognitionInsectDetectionSensitivity
    0x026F: 0xD1F4,  # SubjectRecognitionCarTrainTrackingSubjectShiftRange
    0x0270: 0xD1F5,  # SubjectRecognitionCarTrainTrackingSensitivity
    0x0271: 0xD1F6,  # SubjectRecognitionCarTrainDetectionSensitivity
    0x0272: 0xD1F7,  # SubjectRecognitionPlaneTrackingSubjectShiftRange
    0x0273: 0xD1F8,  # SubjectRecognitionPlaneTrackingSensitivity
    0x0274: 0xD1F9,  # SubjectRecognitionPlaneDetectionSensitivity
    0x0275: 0xD1FA,  # SubjectRecognitionPriorityOnRegisteredFace
    0x0276: 0xD1B8,  # FaceEyeFrameDisplay
    0x0277: 0xD1B9,  # FocusMap
    0x0278: 0xD1BD,  # InitialFocusMagnifier
    0x0279: 0xD1BA,  # AFInFocusMagnifier
    0x027A: 0xD2AD,  # AFTrackForSpeedChange
    0x027B: 0xD138,  # AFFreeSizeAndPositionSetting
    0x027D: 0xD2B2,  # PlaySetOfMultiMedia
    0x027E: 0xD1BE,  # RemoteSaveImageSize
    0x027F: 0xD14A,  # FTP_TransferStillImageQualitySize
    0x0280: 0xD216,  # FTP_AutoTransferTarget_StillImage
    0x0281: 0xD225,  # ProtectImageInFTPTransfer
    0x0282: 0xD1FB,  # MonitorBrightnessType
    0x0283: 0xD1FC,  # MonitorBrightnessManual
    0x0284: 0xD1B0,  # DisplayQualityFinderMonitor
    0x0285: 0xD1FD,  # TCUBDisplaySetting
    0x0286: 0xD1FE,  # GammaDisplayAssist
    0x0287: 0xD1FF,  # GammaDisplayAssistType
    0x0288: 0xD220,  # AudioSignalsStartEnd
    0x0289: 0xD1B1,  # AudioSignalsVolume
    0x028A: 0xD1B2,  # ControlForHDMI
    0x028B: 0xD1B3,  # AntidustShutterWhenPowerOff
    0x028C: 0xD1C1,  # WakeOnLAN
    0x0501: 0xD239,  # reserved10
    0x0502: 0xD23A,  # reserved11
    0x0503: 0xD23B,  # reserved12
    0x0505: 0xD24F,  # Interval_Rec_Mode
    0x0506: 0xD268,  # Still_Image_Trans_Size
    0x0507: 0xD269,  # RAW_J_PC_Save_Image
    0x0508: 0xD26A,  # LiveView_Image_Quality
    0x050C: 0xD299,  # Remocon_Zoom_Speed_Type
    0x0701: 0xD215,  # SnapshotInfo
    0x0702: 0xD218,  # BatteryRemain
    0x0703: 0xD20E,  # BatteryLevel
    0x0704: 0xD214,  # EstimatePictureSize
    0x0705: 0xD21D,  # RecordingState
    0x0706: 0xD221,  # LiveViewStatus
    0x0707: 0xD213,  # FocusIndication
    0x0708: 0xD248,  # MediaSLOT1_Status
    0x0709: 0xD249,  # MediaSLOT1_RemainingNumber
    0x070A: 0xD24A,  # MediaSLOT1_RemainingTime
    0x070B: 0xD279,  # MediaSLOT1_FormatEnableStatus
    0x070C: 0xD27D,  # reserved20
    0x070D: 0xD256,  # MediaSLOT2_Status
    0x070E: 0xD27A,  # MediaSLOT2_FormatEnableStatus
    0x070F: 0xD257,  # MediaSLOT2_RemainingNumber
    0x0710: 0xD258,  # MediaSLOT2_RemainingTime
    0x0711: 0xD27E,  # reserved22
    0x0712: 0xD27B,  # Media_FormatProgressRate
    0x0713: 0xD27F,  # FTP_ConnectionStatus
    0x0714: 0xD280,  # FTP_ConnectionErrorInfo
    0x0715: 0xD267,  # LiveView_Area
    0x0716: 0xD23C,  # reserved26
    0x0717: 0xD23D,  # reserved27
    0x0718: 0xD250,  # Interval_Rec_Status
    0x0719: 0xD270,  # CustomWB_Execution_State
    0x071A: 0xD26B,  # CustomWB_Capturable_Area
    0x071B: 0xD26C,  # CustomWB_Capture_Frame_Size
    0x071C: 0xD26F,  # CustomWB_Capture_Operation
    0x071E: 0xD25B,  # Zoom_Operation_Status
    0x071F: 0xD25D,  # Zoom_Bar_Information
    0x0720: 0xD260,  # Zoom_Type_Status
    0x0721: 0xD292,  # MediaSLOT1_QuickFormatEnableStatus
    0x0722: 0xD293,  # MediaSLOT2_QuickFormatEnableStatus
    0x0723: 0xD294,  # Cancel_Media_FormatEnableStatus
    0x0724: 0xD25E,  # Zoom_Speed_Range
    0x0729: 0xD023,  # IsoCurrentSensitivity
    0x072A: 0xD271,  # CameraSetting_SaveOperationEnableStatus
    0x072B: 0xD272,  # CameraSetting_ReadOperationEnableStatus
    0x072C: 0xD273,  # CameraSetting_SaveRead_State
    0x072D: 0xD043,  # CameraSettingsResetEnableStatus
    0x072E: 0xD29A,  # APS_C_or_Full_SwitchingSetting
    0x072F: 0xD29B,  # APS_C_or_Full_SwitchingEnableStatus
    0x0730: 0xD044,  # DispModeCandidate
    0x0731: 0xD017,  # ShutterSpeedCurrentValue
    0x0732: 0xD008,  # Focus_Speed_Range
    0x0733: 0xD019,  # NDFilterMode
    0x0734: 0xD030,  # MoviePlayingSpeed
    0x0735: 0xD035,  # MediaSLOT1Player
    0x0736: 0xD036,  # MediaSLOT2Player
    0x0737: 0xD038,  # BatteryRemainingInMinutes
    0x0738: 0xD039,  # BatteryRemainingInVoltage
    0x0739: 0xD03E,  # DCVoltage
    0x073A: 0xD02F,  # MoviePlayingState
    0x073B: 0xE004,  # FocusTouchSpotStatus
    0x073C: 0xE005,  # FocusTrackingStatus
    0x073D: 0xE00A,  # DepthOfFieldAdjustmentInterlockingMode
    0x073E: 0xE00B,  # RecorderClipName
    0x073F: 0xE00C,  # RecorderControlMainSetting
    0x0740: 0xE00E,  # RecorderStartMain
    0x0741: 0xE00F,  # RecorderStartProxy
    0x0742: 0xE010,  # RecorderMainStatus
    0x0743: 0xE011,  # RecorderProxyStatus
    0x0744: 0xE012,  # RecorderExtRawStatus
    0x0745: 0xE013,  # RecorderSaveDestination
    0x0746: 0xE035,  # AssignableButtonIndicator1
    0x0747: 0xE036,  # AssignableButtonIndicator2
    0x0748: 0xE037,  # AssignableButtonIndicator3
    0x0749: 0xE038,  # AssignableButtonIndicator4
    0x074A: 0xE039,  # AssignableButtonIndicator5
    0x074B: 0xE03A,  # AssignableButtonIndicator6
    0x074C: 0xE03B,  # AssignableButtonIndicator7
    0x074D: 0xE03C,  # AssignableButtonIndicator8
    0x074E: 0xE03D,  # AssignableButtonIndicator9
    0x077B: 0xE03E,  # AssignableButtonIndicator10
    0x077C: 0xE08F,  # AssignableButtonIndicator11
    0x074F: 0xE03F,  # LensAssignableButtonIndicator1
    0x0750: 0xD01F,  # GaindBCurrentValue
    0x0751: 0xD040,  # SoftwareVersion
    0x0752: 0xE020,  # CurrentSceneFileEdited
    0x0753: 0xE061,  # MovieRecButtonToggleEnableStatus
    0x0754: 0xD284,  # RemoteTouchOperationEnableStatus
    0x0755: 0xD285,  # CancelRemoteTouchOperationEnableStatus
    0x0756: 0xE086,  # LensInformationEnableStatus
    0x0757: 0xE089,  # FollowFocusPositionCurrentValue
    0x0758: 0xD0AB,  # FocusBracketShootingStatus
    0x0759: 0xD0C6,  # PixelMappingEnableStatus
    0x075A: 0xD104,  # TimeCodePresetResetEnableStatus
    0x075B: 0xD105,  # UserBitPresetResetEnableStatus
    0x075C: 0xD106,  # SensorCleaningEnableStatus
    0x075D: 0xD107,  # PictureProfileResetEnableStatus
    0x075E: 0xD108,  # CreativeLookResetEnableStatus
    0x075F: 0xD07D,  # LensVersionNumber
    0x0760: 0xD251,  # DeviceOverheatingState
    0x0761: 0xD11F,  # Movie_IntervalRec_CountDownIntervalTime
    0x0762: 0xD120,  # Movie_IntervalRec_RecordingDuration
    0x0763: 0xD282,  # HighResolutionShutterSpeed
    0x0764: 0xD08B,  # BaseLookImportOperationEnableStatus
    0x0765: 0xD07B,  # LensModelName
    0x0766: 0xE043,  # FocusPositionCurrentValue
    0x0767: 0xD19C,  # FocusDrivingStatus
    0x0768: 0xD2BA,  # FlickerScanStatus
    0x0769: 0xD2BB,  # FlickerScanEnableStatus
    0x076B: 0xD09A,  # FTPServerSettingOperationEnableStatus
    0x076C: 0xD274,  # FTPTransferSetting_SaveOperationEnableStatus
    0x076D: 0xD275,  # FTPTransferSetting_ReadOperationEnableStatus
    0x076E: 0xD276,  # FTPTransferSetting_SaveRead_State
    0x0770: 0xD194,  # CameraShakeStatus
    0x0771: 0xD195,  # UpdateBodyStatus
    0x0773: 0xD197,  # MediaSLOT1_WritingState
    0x0774: 0xD198,  # MediaSLOT2_WritingState
    0x0776: 0xD02B,  # MediaSLOT1_RecordingAvailableType
    0x0777: 0xD02C,  # MediaSLOT2_RecordingAvailableType
    0x0778: 0xD190,  # MediaSLOT3_RecordingAvailableType
    0x0779: 0xD0BC,  # CameraOperatingMode
    0x077A: 0xD0BD,  # PlaybackViewMode
    0x0781: 0xD18E,  # MediaSLOT3_Status
    0x0783: 0xD18F,  # MediaSLOT3_RemainingTime
    0x0786: 0xE098,  # MonitoringDeliveringStatus
    0x0787: 0xE099,  # MonitoringIsDelivering
    0x0788: 0xE09D,  # MonitoringSettingVersion
    0x0789: 0xE09F,  # MonitoringDeliveryTypeSupportInfo
    0x078B: 0xD1BB,  # CameraErrorCautionStatus
    0x078C: 0xD1BC,  # SystemErrorCautionStatus
    0x078D: 0xD20C,  # CameraButtonFunctionStatus
    0x078E: 0xD134,  # FlickerLessShootingStatus
    0x078F: 0xD130,  # ContinuousShootingSpotBoostStatus
    0x0790: 0xD131,  # ContinuousShootingSpotBoostEnableStatus
    0x0791: 0xD19B,  # TimeShiftShootingStatus
    0x0792: 0xD19D,  # ZoomDrivingStatus
    0x0793: 0xD1B4,  # ShootingSelfTimerStatus
    0x0794: 0xD1DB,  # CreateNewFolderEnableStatus
    0x0795: 0xD1C9,  # ForcedFileNumberResetEnableStatus
    0x0796: 0xD19E,  # DefaultAFFreeSizeAndPositionSetting
    0x0797: 0xD1C6,  # TrackingOnAndAFOnEnableStatus
    0x0798: 0xD1BF,  # ProgramShiftStatus
    0x0799: 0xD1B5,  # MeteredManualLevel
    0x079B: 0xD12D,  # SecondBatteryRemain
    0x079C: 0xD12E,  # SecondBatteryLevel
    0x079D: 0xD204,  # TotalBatteryRemain
    0x079E: 0xD205,  # TotalBatteryLevel
    0x028D: 0xD20B,  # CameraLeverFunction
    0x028E: 0xD202,  # ShootingTimingPreNotificationMode
    0x028F: 0xD1DD,  # MicrophoneDirectivity
    0x0290: 0xD1DF,  # ProductShowcaseSet
    0x0291: 0xD1E0,  # AmountOfDefocusSetting
    0x0292: 0xD1E1,  # CinematicVlogSetting
    0x0293: 0xD1E2,  # CinematicVlogLook
    0x0294: 0xD1E3,  # CinematicVlogMood
    0x0295: 0xD1E4,  # CinematicVlogAFTransitionSpeed
    0x07A2: 0xE0A1,  # MonitoringTransportProtocol
    0x07A3: 0xE0A2,  # MonitoringAvailableFormat
    0x07A4: 0xE0A3,  # MonitoringFormatSupportInformation
    0x02BB: 0xE0A4,  # DeSqueezeDisplayRatio
    0x02BC: 0xE040,  # ZoomPositionSetting
    0x07A1: 0xE041,  # ZoomPositionCurrentValue
    0x0F07: 0xE0CF,
    0x0F08: 0xE0D0,
    0x0F09: 0xE0D1,
    0x0F0A: 0xD2B4,
    0x0F0C: 0xE0B3,
    0x0296: 0xD078,  # MonitoringOutputDisplaySDI
    0x07AC: 0xD07A,  # CameraSystemErrorInfo
    0x0297: 0xE079,  # AFAreaPositionAF_C
    0x0298: 0xE078,  # AFAreaPositionAF_S
    0x07AD: 0xD09B,  # FaceEyeDetectionAFStatus
    0x0299: 0xD091,  # AutoFocusHold
    0x029A: 0xD06E,  # PushAFModeSetting
    0x029B: 0xD064,  # TouchFunctionInMF
    0x029C: 0xD05E,  # PushAutoFocus
    0x029D: 0xD05C,  # PushAGC
    0x029E: 0xD05B,  # PushAutoIris
    0x02A3: 0xD077,  # NDFilterPreset3Value
    0x02A2: 0xD076,  # NDFilterPreset2Value
    0x02A1: 0xD075,  # NDFilterPreset1Value
    0x02A0: 0xD074,  # NDFilterPresetSelect
    0x029F: 0xD05D,  # PushAutoNDFilter
    0x02AB: 0xD0AA,  # WhiteBalanceOffsetColorTemp
    0x02AA: 0xD0A9,  # WhiteBalanceOffsetSetting
    0x02A9: 0xD08A,  # WhiteBalanceOffsetTintATW
    0x02A8: 0xD089,  # WhiteBalanceOffsetColorTempATW
    0x02A7: 0xD088,  # WhiteBalanceBGain
    0x02A6: 0xD087,  # WhiteBalanceRGain
    0x02A5: 0xD086,  # WhiteBalancePresetColorTemperature
    0x02A4: 0xD085,  # WhiteBalanceSwitch
    0x02B4: 0xD06D,  # PaintLookDetailLevel
    0x02B3: 0xD06C,  # PaintLookDetailSetting
    0x02B2: 0xD06B,  # PaintLookKneeSlope
    0x02B1: 0xD06A,  # PaintLookKneePoint
    0x02B0: 0xD069,  # PaintLookAutoKnee
    0x02AF: 0xD068,  # PaintLookKneeSetting
    0x02AE: 0xD067,  # PaintLookBBlack
    0x02AD: 0xD066,  # PaintLookRBlack
    0x02AC: 0xD065,  # PaintLookMasterBlack
    0x07AE: 0xD057,  # UploadDatasetVersion
    0x02B5: 0xD2B1,  # UserBaseLookOutput
    0x07AF: 0xD2A9,  # MonitorLUTSettingOutputDestAssign
    0x02B6: 0xD2AA,  # MonitorLUTSetting1
    0x02B7: 0xD2AB,  # MonitorLUTSetting2
    0x02B8: 0xD2AC,  # MonitorLUTSetting3
    0x07B0: 0xD0C1,  # MaximumNumberOfBytes
    0x02B9: 0xD051,  # SQModeSetting
    0x02BA: 0xE0A0,  # MovieQualityFullAutoMode
    0x02BD: 0xD1D0,  # FileSettingsCameraId
    0x02BE: 0xD1D1,  # FileSettingsReelNumber
    0x02BF: 0xD1D2,  # FileSettingsCameraPosition
    0x02C0: 0xD1A9,  # ImageStabilizationFramingStabilizer
    0x02C1: 0xD237,  # ExposureStep
    0x07A0: 0xD2BD,  # TeleWideLeverValueCapability
    0x02C2: 0xE0CD,  # EnlargeScreenSetting
    0x07A5: 0xD1D4,  # MediaSLOT1_ContentsInfoListEnableStatus
    0x07A6: 0xD1D5,  # MediaSLOT2_ContentsInfoListEnableStatus
    0x07A7: 0xD1D6,  # MediaSLOT1_ContentsInfoListRegenerateUpdateTime
    0x07A8: 0xD1D7,  # MediaSLOT2_ContentsInfoListRegenerateUpdateTime
    0x07A9: 0xE0D9,  # MediaSLOT1_ContentsInfoListUpdateTime
    0x07AA: 0xE0DA,  # MediaSLOT2_ContentsInfoListUpdateTime
    0x07AB: 0xD1DA,  # PostViewTransferResourceStatus
    0x02C3: 0xD050,  # SimulRecSetting
    0x02C4: 0xD07F,  # SimulRecSettingMovieRecButton
    0x02C9: 0xD012,  # ShutterSelectMode
    0x02C5: 0xD207,  # OSDImageMode
    0x07B1: 0xD0BF,  # FirmwareUpdateCommandVersion
    0x02C6: 0xE0D5,  # DebugMode
    0x0F0B: 0xD0C0,
    0x02C7: 0xE0DF,  # reserved18
    0x02C8: 0xE0E0,  # reserved19
    0x0F0D: 0xE0C0,
    0x07B5: 0xE0CC,  # SetPresetPTZFBinaryVersion
    0x07B6: 0xE0B7,  # PanPositionStatus
    0x07B7: 0xE0B9,  # TiltPositionStatus
    0x07B8: 0xE0B6,  # PanPositionCurrentValue
    0x07B9: 0xE0B8,  # TiltPositionCurrentValue
    0x02CB: 0xE05C,  # PanTiltAccelerationRampCurve
    0x02CC: 0xE0BE,  # PanLimitMode
    0x02CD: 0xE0BA,  # PanLimitRangeMinimum
    0x02CE: 0xE0BB,  # PanLimitRangeMaximum
    0x02CF: 0xE0BF,  # TiltLimitMode
    0x02D0: 0xE0BC,  # TiltLimitRangeMinimum
    0x02D1: 0xE0BD,  # TiltLimitRangeMaximum
    0x02D2: 0xE0CB,  # PresetPTZFSlotNumber
    0x07BA: 0xE0AF,  # CameraPowerStatus
    0x0313: 0xD2BE,  # TargetStreamingDestinationSelect
    0x07CD: 0xD119,  # StreamStatus
    0x02D3: 0xE0A5,  # IRRemoteSetting
    0x02D4: 0xE0A6,  # IPSetupProtocolSetting
    0x07BB: 0xE0B0,  # RecordablePowerSources
    0x07CF: 0xD1CC,  # StreamSettingListOperationStatus
    0x02E4: 0xD29E,  # PaintLookMultiMatrixAreaIndication
    0x02D5: 0xD002,  # IrisCloseSetting
    0x07BC: 0xD080,  # DisplayedMenuStatus
    0x02D6: 0xD08F,  # LanguageSetting
    0x07BD: 0xD09C,  # PlaybackContentsRecordingDateTime
    0x07BE: 0xD09D,  # PlaybackContentsName
    0x07BF: 0xD09E,  # PlaybackContentsNumber
    0x07C0: 0xD09F,  # PlaybackContentsTotalNumber
    0x07C1: 0xD0A0,  # PlaybackContentsRecordingResolution
    0x07C2: 0xD0A1,  # PlaybackContentsRecordingFrameRate
    0x07C3: 0xD0A2,  # PlaybackContentsRecordingFileFormat
    0x07C4: 0xD0A4,  # PlaybackContentsGammaType
    0x07C5: 0xD0C3,  # BaseLookNameofPlayback
    0x07C6: 0xD0C4,  # BaseLookAppliedofPlayback
    0x02D7: 0xD139,  # PaintLookUserMatrixSetting
    0x02D8: 0xD13A,  # PaintLookUserMatrixLevel
    0x02D9: 0xD13B,  # PaintLookUserMatrixPhase
    0x02DA: 0xD13C,  # PaintLookUserMatrixRG
    0x02DB: 0xD13D,  # PaintLookUserMatrixRB
    0x02DC: 0xD13E,  # PaintLookUserMatrixGR
    0x02DD: 0xD13F,  # PaintLookUserMatrixGB
    0x02DE: 0xD140,  # PaintLookUserMatrixBR
    0x02DF: 0xD141,  # PaintLookUserMatrixBG
    0x02E0: 0xD142,  # PaintLookMultiMatrixSetting
    0x02E1: 0xD143,  # PaintLookMultiMatrixAxis
    0x02E2: 0xD144,  # PaintLookMultiMatrixHue
    0x02E3: 0xD145,  # PaintLookMultiMatrixSaturation
    0x07C7: 0xD2AE,  # MonitoringOutputDisplaySettingDestAssign
    0x02FC: 0xD2AF,  # MonitoringOutputDisplaySetting1
    0x02FD: 0xD2B0,  # MonitoringOutputDisplaySetting2
    0x07C8: 0xE044,  # FocusModeStatus
    0x07C9: 0xE045,  # FocusOperationWithInt16EnableStatus
    0x02E5: 0xE048,  # AudioInputCH1LevelControl
    0x02E6: 0xE049,  # AudioInputCH2LevelControl
    0x02E7: 0xE04A,  # AudioInputCH3LevelControl
    0x02E8: 0xE04B,  # AudioInputCH4LevelControl
    0x02E9: 0xE04C,  # AudioInputCH1Level
    0x02EA: 0xE04D,  # AudioInputCH2Level
    0x02EB: 0xE04E,  # AudioInputCH3Level
    0x02EC: 0xE04F,  # AudioInputCH4Level
    0x02ED: 0xE051,  # AudioInputCH1InputSelect
    0x02EE: 0xE052,  # AudioInputCH2InputSelect
    0x02EF: 0xE053,  # AudioInputCH3InputSelect
    0x02F0: 0xE054,  # AudioInputCH4InputSelect
    0x02F1: 0xE055,  # AudioInputCH1WindFilter
    0x02F2: 0xE056,  # AudioInputCH2WindFilter
    0x02F3: 0xE057,  # AudioInputCH3WindFilter
    0x02F4: 0xE058,  # AudioInputCH4WindFilter
    0x02F7: 0xE05F,  # RemoteKeyThumbnailButton
    0x02F8: 0xE060,  # RemoteKeySLOTSelectButton
    0x02F9: 0xE067,  # VideoRecordingFormatBitrateSetting
    0x07CA: 0xE068,  # ValidRecordingVideoFormat
    0x02FB: 0xE06C,  # MonitoringOutputFormat
    0x02FE: 0xE092,  # FocusSpeedDirectSync
    0x02F5: 0xE0AA,  # AudioInput1TypeSelect
    0x02F6: 0xE0AB,  # AudioInput2TypeSelect
    0x02FA: 0xE0B5,  # VideoRecordingFormatQuality
    0x02FF: 0xE0CE,  # LiveViewImageQualityByNumericalValue
    0x0300: 0xE0D2,  # TallyLampControlRed
    0x0301: 0xE0D3,  # TallyLampControlGreen
    0x0302: 0xE0D4,  # TallyLampControlYellow
    0x0305: 0xD026,  # Movie_RecordingResolutionForRTSP
    0x0307: 0xD02D,  # Movie_RecordingFrameRateRTSPSetting
    0x0308: 0xD053,  # PictureCacheRecSetting
    0x0309: 0xD054,  # PictureCacheRecSizeAndTime
    0x030A: 0xD056,  # Movie_IntervalRecFrames
    0x030B: 0xD05F,  # ImagerScanMode
    0x0306: 0xD063,  # Movie_RecordingResolutionForRAW
    0x07CB: 0xD07C,  # LensSerialNumber
    0x030C: 0xE0FA,  # ShootingEnableSettingLicense
    0x030D: 0xE10E,  # GridLineDisplayPlayback
    0x030E: 0xE10F,  # GridLineType
    0x07D9: 0xE110,  # CustomGridLineFileCommandVersion
    0x07CC: 0xE0FE,  # MaximumSizeOfImageIDString
    0x07CE: 0xE112,  # StreamButtonEnableStatus
    0x07B3: 0xD229,  # AutoRecognitionTargetCandidates
    0x02CA: 0xD234,  # AutoRecognitionTargetSetting
    0x07D3: 0xE0F3,  # DeleteContentOperationEnableStatusSLOT1
    0x07D4: 0xE0F4,  # DeleteContentOperationEnableStatusSLOT2
    0x030F: 0xE0F5,  # DifferentSetForSQMovie
    0x0310: 0xE0E2,  # ManualInputForNDFilterValue
    0x0311: 0xE0E3,  # LogShootingMode
    0x0312: 0xE0E4,  # LogShootingModeColorGamut
    0x0315: 0xD0AC,  # VideoStreamSelect
    0x0314: 0xD2BF,  # StreamDisplayName
    0x0316: 0xD0AE,  # VideoStreamResolution
    0x0317: 0xD2C0,  # VideoStreamMaxBitRate
    0x0318: 0xD10E,  # VideoStreamAdaptiveRateControl
    0x0319: 0xD0AD,  # VideoStreamCodec
    0x031A: 0xD116,  # StreamLatency
    0x031B: 0xD117,  # StreamTTL
    0x031C: 0xD113,  # StreamCipherType
    0x031D: 0xD118,  # StreamModeSetting
    0x031E: 0xD10F,  # VideoStreamResolutionMethod
    0x031F: 0xD11A,  # VideoStreamMovieRecPermission
    0x0320: 0xD0B5,  # VideoStreamBitRateCompressionMode
    0x0321: 0xD2B3,  # VideoStreamBitRateVBRMode
    0x0322: 0xD11B,  # AudioStreamCodecType
    0x0323: 0xD11C,  # AudioStreamSamplingFrequency
    0x0324: 0xD11D,  # AudioStreamBitDepth
    0x0325: 0xD11E,  # AudioStreamChannel
    0x0326: 0xE111,  # HomeMenuSetting
    0x0327: 0xE0E1,  # CallSetting
    0x0328: 0xE0E5,  # NDFilterPositionSetting
    0x07D5: 0xE0E6,  # SceneFileCommandVersion
    0x07D6: 0xE101,  # SceneFileUploadOperationEnableStatus
    0x07D7: 0xE102,  # SceneFileDownloadOperationEnableStatus
    0x07D8: 0xE0F9,  # SceneFileIndexesAvailableForDownload
    0x07D1: 0xD122,  # EframingType
    0x07D2: 0xD123,  # EframingCommandVersion
    0x0329: 0xE0F8,  # EframingAutoFraming
    0x032A: 0xE0F0,  # EframingTrackingStartMode
    0x032B: 0xE0F1,  # EframingProductionEffect
    0x032C: 0xD127,  # EframingSpeedPTZ
    0x0601: 0xD009,
    0x0331: 0xD18C,  # TopOfTheGroupShootingMarkSetting
    0x0603: 0xD18D,
    0x0332: 0xD148,  # CompRAWShootingNR
    0x0333: 0xD149,  # CompRAWShootingNRFileCompressionType
    0x0334: 0xD15A,  # CompRAWShootingNRNumberOfSheets
    0x07DA: 0xD2A6,  # ElapsedBulbExposureTime
    0x07DB: 0xD2A7,  # RemainingBulbExposureTime
    0x07DC: 0xD2A8,  # RemainingNoiseReductionTime
    0x0F01: 0xD261,
    0x0F02: 0xD22A,
    0x032D: 0xE100,  # DigitalExtenderMagnificationSetting
    0x032E: 0xE07A,  # MovieRecReviewPlayingState
    0x011F: 0xD2D1,  # NearFar
    0x0120: 0xD2D2,  # reserved7
    0x0121: 0xD2DC,  # AF_Area_Position
    0x0126: 0xD2DD,  # Zoom_Operation
    0x0134: 0xD2E9,  # ZoomAndFocusPosition_Save
    0x0135: 0xD2EA,  # ZoomAndFocusPosition_Load
    0x015B: 0xD2EC,  # ColortempStep
    0x015E: 0xD2ED,  # WhiteBalanceTintStep
    0x015F: 0xD2EF,  # Focus_Operation
    0x0162: 0xF000,  # ShutterECSNumberStep
    0x0193: 0xD2E4,  # RemoteTouchOperation
    0x027C: 0xD2F2,  # ZoomAndFocusPresetZoomOnly_Set
    0x0509: 0xD2DF,  # CustomWB_Capture_Standby
    0x050A: 0xD2E0,  # CustomWB_Capture_Standby_Cancel
    0x050B: 0xD2E1,  # CustomWB_Capture
    0x0303: 0xF003,  # ZoomOperationWithInt16
    0x0304: 0xF004,  # FocusOperationWithInt16
    0x032F: 0xD2E3,  # HighResolutionShutterSpeedAdjust
    0x0330: 0xD2F0,  # HighResolutionShutterSpeedAdjustInIntegralMultiples
    0x034B: 0xE0F6,  # Movie_AngleOfViewPriority
    0x034C: 0xE0D6,  # WindNoiseReductForExternalMic
    0x034D: 0xE0D7,  # NoiseCutFilter
    0x034E: 0xE0D8,  # NoiseCutFilterForExternalMic
    0x07DD: 0xE107,  # DispModeCandidateStill
    0x0339: 0xE108,  # DispModeSettingStill
    0x033A: 0xE109,  # DispModeStill
    0x07DE: 0xE10A,  # DispModeCandidateMovie
    0x033B: 0xE10B,  # DispModeSettingMovie
    0x033C: 0xE10C,  # DispModeMovie
    0x0335: 0xE0DB,  # CompRAWShootingHDR
    0x0338: 0xE0DC,  # CompRAWShootingHDRDRSetting
    0x0336: 0xE0DD,  # CompRAWShootingHDRFileCompressionType
    0x0337: 0xE0DE,  # CompRAWShootingHDRNumberOfSheets
    0x07DF: 0xE081,  # ControlGeneralSettingFileEnableStatus
    0x033D: 0xE11A,  # PeakingDisplay
    0x033E: 0xE11B,  # PeakingLevel
    0x033F: 0xE11C,  # PeakingColor
    0x0340: 0xE11D,  # ZebraDisplay
    0x0341: 0xE11E,  # ZebraLevel
    0x0342: 0xE11F,  # ZebraLevelTypeCustom
    0x0343: 0xE120,  # ZebraLevelStandardCustom
    0x0344: 0xE121,  # ZebraLevelRangeCustom
    0x0345: 0xE122,  # ZebraLevelLowerLimitCustom
    0x0346: 0xE123,  # MarkerDisplay
    0x0347: 0xE124,  # CenterMarkerDisplay
    0x0348: 0xE125,  # AspectMarkerRatioMovie
    0x0349: 0xE126,  # SafetyZoneDisplay
    0x034A: 0xE127,  # GuideframeDisplay
    0x034F: 0xE12A,  # DualGain
    0x0350: 0xE131,  # ImagerMode
    0x0351: 0xE133,  # DisplayQualityForFinderOnly
    0x0352: 0xE134,  # DisplayQualityForMonitorOnly
    0x0F06: 0xD264,
    0x0602: 0xD1C2,
    0x0F03: 0xD1C3,
    0x0F04: 0xD1C4,
    0x0F05: 0xD1C5,
}


WIRE_TO_CRSDK = {v: k for k, v in CRSDK_TO_WIRE.items()}


PROPERTY_NAMES = {
    0x0100: "FNumber",
    0x0101: "ExposureBiasCompensation",
    0x0102: "FlashCompensation",
    0x0103: "ShutterSpeed",
    0x0104: "IsoSensitivity",
    0x0105: "ExposureProgramMode",
    0x0106: "FileType",
    0x012B: "MediaSLOT1_FileType",
    0x012C: "MediaSLOT2_FileType",
    0x0107: "StillImageQuality",
    0x012D: "MediaSLOT1_ImageQuality",
    0x012E: "MediaSLOT2_ImageQuality",
    0x0108: "WhiteBalance",
    0x0109: "FocusMode",
    0x010A: "MeteringMode",
    0x010B: "FlashMode",
    0x010C: "WirelessFlash",
    0x010D: "RedEyeReduction",
    0x010E: "DriveMode",
    0x010F: "DRO",
    0x0110: "ImageSize",
    0x012F: "MediaSLOT1_ImageSize",
    0x0130: "MediaSLOT2_ImageSize",
    0x0111: "AspectRatio",
    0x0112: "PictureEffect",
    0x0113: "FocusArea",
    0x0114: "reserved4",
    0x0115: "Colortemp",
    0x0116: "ColorTuningAB",
    0x0117: "ColorTuningGM",
    0x0118: "LiveViewDisplayEffect",
    0x0119: "StillImageStoreDestination",
    0x011A: "PriorityKeySettings",
    0x011B: "AFTrackingSensitivity",
    0x011D: "Focus_Magnifier_Setting",
    0x011E: "DateTime_Settings",
    0x0124: "Zoom_Scale",
    0x0125: "Zoom_Setting",
    0x0127: "Movie_File_Format",
    0x0128: "Movie_Recording_Setting",
    0x0129: "Movie_Recording_FrameRateSetting",
    0x012A: "CompressionFileFormatStill",
    0x0131: "RAW_FileCompressionType",
    0x0132: "MediaSLOT1_RAW_FileCompressionType",
    0x0133: "MediaSLOT2_RAW_FileCompressionType",
    0x0136: "IrisModeSetting",
    0x0137: "ShutterModeSetting",
    0x0138: "GainControlSetting",
    0x0139: "GainBaseIsoSensitivity",
    0x013A: "GainBaseSensitivity",
    0x013B: "ExposureIndex",
    0x013C: "BaseLookValue",
    0x013D: "PlaybackMedia",
    0x013E: "DispModeSetting",
    0x013F: "DispMode",
    0x0140: "TouchOperation",
    0x0141: "SelectFinderMonitor",
    0x0142: "AutoPowerOffTemperature",
    0x0143: "BodyKeyLock",
    0x0144: "ImageID_Num_Setting",
    0x0145: "ImageID_Num",
    0x0146: "ImageID_String",
    0x0147: "ExposureCtrlType",
    0x0148: "MonitorLUTSetting",
    0x0149: "FocalDistanceInMeter",
    0x014A: "FocalDistanceInFeet",
    0x014B: "FocalDistanceUnitSetting",
    0x014C: "DigitalZoomScale",
    0x014D: "ZoomDistance",
    0x014E: "ZoomDistanceUnitSetting",
    0x014F: "ShutterModeStatus",
    0x0150: "ShutterSlow",
    0x0151: "ShutterSlowFrames",
    0x0152: "Movie_Recording_ResolutionForMain",
    0x0153: "Movie_Recording_ResolutionForProxy",
    0x0154: "Movie_Recording_FrameRateProxySetting",
    0x0155: "BatteryRemainDisplayUnit",
    0x0156: "PowerSource",
    0x0157: "MovieShootingMode",
    0x0158: "MovieShootingModeColorGamut",
    0x0159: "MovieShootingModeTargetDisplay",
    0x015A: "DepthOfFieldAdjustmentMode",
    0x015C: "WhiteBalanceModeSetting",
    0x015D: "WhiteBalanceTint",
    0x0160: "ShutterECSSetting",
    0x0161: "ShutterECSNumber",
    0x0163: "ShutterECSFrequency",
    0x0164: "RecorderControlProxySetting",
    0x0165: "ButtonAssignmentAssignable1",
    0x0166: "ButtonAssignmentAssignable2",
    0x0167: "ButtonAssignmentAssignable3",
    0x0168: "ButtonAssignmentAssignable4",
    0x0169: "ButtonAssignmentAssignable5",
    0x016A: "ButtonAssignmentAssignable6",
    0x016B: "ButtonAssignmentAssignable7",
    0x016C: "ButtonAssignmentAssignable8",
    0x016D: "ButtonAssignmentAssignable9",
    0x021F: "ButtonAssignmentAssignable10",
    0x0220: "ButtonAssignmentAssignable11",
    0x016E: "ButtonAssignmentLensAssignable1",
    0x016F: "AssignableButton1",
    0x0170: "AssignableButton2",
    0x0171: "AssignableButton3",
    0x0172: "AssignableButton4",
    0x0173: "AssignableButton5",
    0x0174: "AssignableButton6",
    0x0175: "AssignableButton7",
    0x0176: "AssignableButton8",
    0x0177: "AssignableButton9",
    0x0225: "AssignableButton10",
    0x0226: "AssignableButton11",
    0x0178: "LensAssignableButton1",
    0x0179: "FocusModeSetting",
    0x017A: "ShutterAngle",
    0x017B: "ShutterSetting",
    0x017C: "ShutterMode",
    0x017D: "ShutterSpeedValue",
    0x017E: "NDFilter",
    0x017F: "NDFilterModeSetting",
    0x0180: "NDFilterValue",
    0x0181: "GainUnitSetting",
    0x0182: "GaindBValue",
    0x0183: "AWB",
    0x0184: "SceneFileIndex",
    0x0185: "MoviePlayButton",
    0x0186: "MoviePlayPauseButton",
    0x0187: "MoviePlayStopButton",
    0x0188: "MovieForwardButton",
    0x0189: "MovieRewindButton",
    0x018A: "MovieNextButton",
    0x018B: "MoviePrevButton",
    0x018C: "MovieRecReviewButton",
    0x018D: "SubjectRecognitionAF",
    0x018E: "AFTransitionSpeed",
    0x018F: "AFSubjShiftSens",
    0x0190: "AFAssist",
    0x0191: "NDFilterSwitchingSetting",
    0x0192: "FunctionOfRemoteTouchOperation",
    0x0194: "FollowFocusPositionSetting",
    0x0195: "FocusBracketShotNumber",
    0x0196: "FocusBracketFocusRange",
    0x0197: "ExtendedInterfaceMode",
    0x0198: "SQRecordingFrameRateSetting",
    0x0199: "SQFrameRate",
    0x019A: "SQRecordingSetting",
    0x019B: "AudioRecording",
    0x019C: "AudioInputMasterLevel",
    0x019D: "TimeCodePreset",
    0x019E: "TimeCodeFormat",
    0x019F: "TimeCodeRun",
    0x01A0: "TimeCodeMake",
    0x01A1: "UserBitPreset",
    0x01A2: "UserBitTimeRec",
    0x01A3: "ImageStabilizationSteadyShot",
    0x01A4: "Movie_ImageStabilizationSteadyShot",
    0x01A5: "SilentMode",
    0x01A6: "SilentModeApertureDriveInAF",
    0x01A7: "SilentModeShutterWhenPowerOff",
    0x01A8: "SilentModeAutoPixelMapping",
    0x01A9: "ShutterType",
    0x01AA: "PictureProfile",
    0x01AB: "PictureProfile_BlackLevel",
    0x01AC: "PictureProfile_Gamma",
    0x01AD: "PictureProfile_BlackGammaRange",
    0x01AE: "PictureProfile_BlackGammaLevel",
    0x01AF: "PictureProfile_KneeMode",
    0x01B0: "PictureProfile_KneeAutoSet_MaxPoint",
    0x01B1: "PictureProfile_KneeAutoSet_Sensitivity",
    0x01B2: "PictureProfile_KneeManualSet_Point",
    0x01B3: "PictureProfile_KneeManualSet_Slope",
    0x01B4: "PictureProfile_ColorMode",
    0x01B5: "PictureProfile_Saturation",
    0x01B6: "PictureProfile_ColorPhase",
    0x01B7: "PictureProfile_ColorDepthRed",
    0x01B8: "PictureProfile_ColorDepthGreen",
    0x01B9: "PictureProfile_ColorDepthBlue",
    0x01BA: "PictureProfile_ColorDepthCyan",
    0x01BB: "PictureProfile_ColorDepthMagenta",
    0x01BC: "PictureProfile_ColorDepthYellow",
    0x01BD: "PictureProfile_DetailLevel",
    0x01BE: "PictureProfile_DetailAdjustMode",
    0x01BF: "PictureProfile_DetailAdjustVHBalance",
    0x01C0: "PictureProfile_DetailAdjustBWBalance",
    0x01C1: "PictureProfile_DetailAdjustLimit",
    0x01C2: "PictureProfile_DetailAdjustCrispening",
    0x01C3: "PictureProfile_DetailAdjustHiLightDetail",
    0x01C4: "PictureProfile_Copy",
    0x01C5: "CreativeLook",
    0x01C6: "CreativeLook_Contrast",
    0x01C7: "CreativeLook_Highlights",
    0x01C8: "CreativeLook_Shadows",
    0x01C9: "CreativeLook_Fade",
    0x01CA: "CreativeLook_Saturation",
    0x01CB: "CreativeLook_Sharpness",
    0x01CC: "CreativeLook_SharpnessRange",
    0x01CD: "CreativeLook_Clarity",
    0x01CE: "CreativeLook_CustomLook",
    0x01CF: "Movie_ProxyFileFormat",
    0x01D0: "ProxyRecordingSetting",
    0x01D1: "FunctionOfTouchOperation",
    0x01D2: "HighResolutionShutterSpeedSetting",
    0x01D3: "DeleteUserBaseLook",
    0x01D4: "SelectUserBaseLookToEdit",
    0x01D5: "SelectUserBaseLookToSetInPPLUT",
    0x01D6: "UserBaseLookInput",
    0x01D7: "UserBaseLookAELevelOffset",
    0x01D8: "BaseISOSwitchEI",
    0x01D9: "FlickerLessShooting",
    0x01DA: "AudioLevelDisplay",
    0x01DB: "PlaybackVolumeSettings",
    0x01DC: "AutoReview",
    0x01DD: "AudioSignals",
    0x01DE: "HDMIResolutionStillPlay",
    0x01DF: "Movie_HDMIOutputRecMedia",
    0x01E0: "Movie_HDMIOutputResolution",
    0x01E1: "Movie_HDMIOutput4KSetting",
    0x01E2: "Movie_HDMIOutputRAW",
    0x01E3: "Movie_HDMIOutputRawSetting",
    0x01E4: "Movie_HDMIOutputColorGamutForRAWOut",
    0x01E5: "Movie_HDMIOutputTimeCode",
    0x01E6: "Movie_HDMIOutputRecControl",
    0x01E8: "MonitoringOutputDisplayHDMI",
    0x01E9: "Movie_HDMIOutputAudioCH",
    0x01EA: "Movie_IntervalRec_IntervalTime",
    0x01EB: "Movie_IntervalRec_FrameRateSetting",
    0x01EC: "Movie_IntervalRec_RecordingSetting",
    0x01ED: "EframingScaleAuto",
    0x01EE: "EframingSpeedAuto",
    0x01EF: "EframingModeAuto",
    0x01F0: "EframingRecordingImageCrop",
    0x01F1: "EframingHDMICrop",
    0x01F2: "CameraEframing",
    0x01F3: "USBPowerSupply",
    0x01F4: "LongExposureNR",
    0x01F5: "HighIsoNR",
    0x01F6: "HLGStillImage",
    0x01F7: "ColorSpace",
    0x01F8: "BracketOrder",
    0x01F9: "FocusBracketOrder",
    0x01FA: "FocusBracketExposureLock1stImg",
    0x01FB: "FocusBracketIntervalUntilNextShot",
    0x01FC: "IntervalRec_ShootingStartTime",
    0x01FD: "IntervalRec_ShootingInterval",
    0x01FE: "IntervalRec_ShootIntervalPriority",
    0x01FF: "IntervalRec_NumberOfShots",
    0x0200: "IntervalRec_AETrackingSensitivity",
    0x0201: "IntervalRec_ShutterType",
    0x0202: "ElectricFrontCurtainShutter",
    0x0203: "WindNoiseReduct",
    0x0204: "RecordingSelfTimer",
    0x0205: "RecordingSelfTimerCountTime",
    0x0206: "RecordingSelfTimerContinuous",
    0x0207: "RecordingSelfTimerStatus",
    0x0208: "BulbTimerSetting",
    0x0209: "BulbExposureTimeSetting",
    0x020A: "AutoSlowShutter",
    0x020B: "IsoAutoMinShutterSpeedMode",
    0x020C: "IsoAutoMinShutterSpeedManual",
    0x020D: "IsoAutoMinShutterSpeedPreset",
    0x020E: "FocusPositionSetting",
    0x020F: "SoftSkinEffect",
    0x0210: "PrioritySetInAF_S",
    0x0211: "PrioritySetInAF_C",
    0x0212: "FocusMagnificationTime",
    0x0213: "SubjectRecognitionInAF",
    0x0214: "RecognitionTarget",
    0x0215: "RightLeftEyeSelect",
    0x0216: "SelectFTPServer",
    0x0217: "SelectFTPServerID",
    0x0218: "FTP_Function",
    0x0219: "FTP_AutoTransfer",
    0x021A: "FTP_AutoTransferTarget",
    0x021B: "Movie_FTP_AutoTransferTarget",
    0x021C: "FTP_TransferTarget",
    0x021D: "Movie_FTP_TransferTarget",
    0x021E: "FTP_PowerSave",
    0x022B: "NDFilterUnitSetting",
    0x022C: "NDFilterOpticalDensityValue",
    0x022D: "TNumber",
    0x022E: "IrisDisplayUnit",
    0x022F: "Movie_ImageStabilizationLevel",
    0x0230: "ImageStabilizationSteadyShotAdjust",
    0x0231: "ImageStabilizationSteadyShotFocalLength",
    0x0232: "ExtendedShutterSpeed",
    0x0233: "CameraButtonFunction",
    0x0234: "CameraButtonFunctionMulti",
    0x0235: "CameraDialFunction",
    0x0236: "SynchroterminalForcedOutput",
    0x0237: "ShutterReleaseTimeLagControl",
    0x0238: "ContinuousShootingSpotBoostFrameSpeed",
    0x0239: "TimeShiftShooting",
    0x023A: "TimeShiftTriggerSetting",
    0x023B: "TimeShiftPreShootingTimeSetting",
    0x023C: "EmbedLUTFile",
    0x023D: "APS_C_S35",
    0x023E: "LensCompensationShading",
    0x023F: "LensCompensationChromaticAberration",
    0x0240: "LensCompensationDistortion",
    0x0241: "LensCompensationBreathing",
    0x0242: "RecordingMedia",
    0x0243: "Movie_RecordingMedia",
    0x0244: "AutoSwitchMedia",
    0x0245: "RecordingFileNumber",
    0x0246: "Movie_RecordingFileNumber",
    0x0247: "RecordingSettingFileName",
    0x0248: "RecordingFolderFormat",
    0x024A: "SelectIPTCMetadata",
    0x024B: "WriteCopyrightInfo",
    0x024C: "SetPhotographer",
    0x024D: "SetCopyright",
    0x024E: "FileSettingsTitleNameSettings",
    0x024F: "FocusBracketRecordingFolder",
    0x0250: "ReleaseWithoutLens",
    0x0251: "ReleaseWithoutCard",
    0x0252: "GridLineDisplay",
    0x0253: "ContinuousShootingSpeedInElectricShutterHiPlus",
    0x0254: "ContinuousShootingSpeedInElectricShutterHi",
    0x0255: "ContinuousShootingSpeedInElectricShutterMid",
    0x0256: "ContinuousShootingSpeedInElectricShutterLo",
    0x0257: "IsoAutoRangeLimitMin",
    0x0258: "IsoAutoRangeLimitMax",
    0x0259: "FacePriorityInMultiMetering",
    0x025A: "PrioritySetInAWB",
    0x025B: "CustomWB_Size_Setting",
    0x025C: "AFIlluminator",
    0x025D: "ApertureDriveInAF",
    0x025E: "AFWithShutter",
    0x025F: "FullTimeDMF",
    0x0260: "PreAF",
    0x0261: "SubjectRecognitionPersonTrackingSubjectShiftRange",
    0x0262: "SubjectRecognitionAnimalBirdPriority",
    0x0263: "SubjectRecognitionAnimalBirdDetectionParts",
    0x0264: "SubjectRecognitionAnimalTrackingSubjectShiftRange",
    0x0265: "SubjectRecognitionAnimalTrackingSensitivity",
    0x0266: "SubjectRecognitionAnimalDetectionSensitivity",
    0x0267: "SubjectRecognitionAnimalDetectionParts",
    0x0268: "SubjectRecognitionBirdTrackingSubjectShiftRange",
    0x0269: "SubjectRecognitionBirdTrackingSensitivity",
    0x026A: "SubjectRecognitionBirdDetectionSensitivity",
    0x026B: "SubjectRecognitionBirdDetectionParts",
    0x026C: "SubjectRecognitionInsectTrackingSubjectShiftRange",
    0x026D: "SubjectRecognitionInsectTrackingSensitivity",
    0x026E: "SubjectRecognitionInsectDetectionSensitivity",
    0x026F: "SubjectRecognitionCarTrainTrackingSubjectShiftRange",
    0x0270: "SubjectRecognitionCarTrainTrackingSensitivity",
    0x0271: "SubjectRecognitionCarTrainDetectionSensitivity",
    0x0272: "SubjectRecognitionPlaneTrackingSubjectShiftRange",
    0x0273: "SubjectRecognitionPlaneTrackingSensitivity",
    0x0274: "SubjectRecognitionPlaneDetectionSensitivity",
    0x0275: "SubjectRecognitionPriorityOnRegisteredFace",
    0x0276: "FaceEyeFrameDisplay",
    0x0277: "FocusMap",
    0x0278: "InitialFocusMagnifier",
    0x0279: "AFInFocusMagnifier",
    0x027A: "AFTrackForSpeedChange",
    0x027B: "AFFreeSizeAndPositionSetting",
    0x027D: "PlaySetOfMultiMedia",
    0x027E: "RemoteSaveImageSize",
    0x027F: "FTP_TransferStillImageQualitySize",
    0x0280: "FTP_AutoTransferTarget_StillImage",
    0x0281: "ProtectImageInFTPTransfer",
    0x0282: "MonitorBrightnessType",
    0x0283: "MonitorBrightnessManual",
    0x0284: "DisplayQualityFinderMonitor",
    0x0285: "TCUBDisplaySetting",
    0x0286: "GammaDisplayAssist",
    0x0287: "GammaDisplayAssistType",
    0x0288: "AudioSignalsStartEnd",
    0x0289: "AudioSignalsVolume",
    0x028A: "ControlForHDMI",
    0x028B: "AntidustShutterWhenPowerOff",
    0x028C: "WakeOnLAN",
    0x0501: "reserved10",
    0x0502: "reserved11",
    0x0503: "reserved12",
    0x0505: "Interval_Rec_Mode",
    0x0506: "Still_Image_Trans_Size",
    0x0507: "RAW_J_PC_Save_Image",
    0x0508: "LiveView_Image_Quality",
    0x050C: "Remocon_Zoom_Speed_Type",
    0x0701: "SnapshotInfo",
    0x0702: "BatteryRemain",
    0x0703: "BatteryLevel",
    0x0704: "EstimatePictureSize",
    0x0705: "RecordingState",
    0x0706: "LiveViewStatus",
    0x0707: "FocusIndication",
    0x0708: "MediaSLOT1_Status",
    0x0709: "MediaSLOT1_RemainingNumber",
    0x070A: "MediaSLOT1_RemainingTime",
    0x070B: "MediaSLOT1_FormatEnableStatus",
    0x070C: "reserved20",
    0x070D: "MediaSLOT2_Status",
    0x070E: "MediaSLOT2_FormatEnableStatus",
    0x070F: "MediaSLOT2_RemainingNumber",
    0x0710: "MediaSLOT2_RemainingTime",
    0x0711: "reserved22",
    0x0712: "Media_FormatProgressRate",
    0x0713: "FTP_ConnectionStatus",
    0x0714: "FTP_ConnectionErrorInfo",
    0x0715: "LiveView_Area",
    0x0716: "reserved26",
    0x0717: "reserved27",
    0x0718: "Interval_Rec_Status",
    0x0719: "CustomWB_Execution_State",
    0x071A: "CustomWB_Capturable_Area",
    0x071B: "CustomWB_Capture_Frame_Size",
    0x071C: "CustomWB_Capture_Operation",
    0x071E: "Zoom_Operation_Status",
    0x071F: "Zoom_Bar_Information",
    0x0720: "Zoom_Type_Status",
    0x0721: "MediaSLOT1_QuickFormatEnableStatus",
    0x0722: "MediaSLOT2_QuickFormatEnableStatus",
    0x0723: "Cancel_Media_FormatEnableStatus",
    0x0724: "Zoom_Speed_Range",
    0x0729: "IsoCurrentSensitivity",
    0x072A: "CameraSetting_SaveOperationEnableStatus",
    0x072B: "CameraSetting_ReadOperationEnableStatus",
    0x072C: "CameraSetting_SaveRead_State",
    0x072D: "CameraSettingsResetEnableStatus",
    0x072E: "APS_C_or_Full_SwitchingSetting",
    0x072F: "APS_C_or_Full_SwitchingEnableStatus",
    0x0730: "DispModeCandidate",
    0x0731: "ShutterSpeedCurrentValue",
    0x0732: "Focus_Speed_Range",
    0x0733: "NDFilterMode",
    0x0734: "MoviePlayingSpeed",
    0x0735: "MediaSLOT1Player",
    0x0736: "MediaSLOT2Player",
    0x0737: "BatteryRemainingInMinutes",
    0x0738: "BatteryRemainingInVoltage",
    0x0739: "DCVoltage",
    0x073A: "MoviePlayingState",
    0x073B: "FocusTouchSpotStatus",
    0x073C: "FocusTrackingStatus",
    0x073D: "DepthOfFieldAdjustmentInterlockingMode",
    0x073E: "RecorderClipName",
    0x073F: "RecorderControlMainSetting",
    0x0740: "RecorderStartMain",
    0x0741: "RecorderStartProxy",
    0x0742: "RecorderMainStatus",
    0x0743: "RecorderProxyStatus",
    0x0744: "RecorderExtRawStatus",
    0x0745: "RecorderSaveDestination",
    0x0746: "AssignableButtonIndicator1",
    0x0747: "AssignableButtonIndicator2",
    0x0748: "AssignableButtonIndicator3",
    0x0749: "AssignableButtonIndicator4",
    0x074A: "AssignableButtonIndicator5",
    0x074B: "AssignableButtonIndicator6",
    0x074C: "AssignableButtonIndicator7",
    0x074D: "AssignableButtonIndicator8",
    0x074E: "AssignableButtonIndicator9",
    0x077B: "AssignableButtonIndicator10",
    0x077C: "AssignableButtonIndicator11",
    0x074F: "LensAssignableButtonIndicator1",
    0x0750: "GaindBCurrentValue",
    0x0751: "SoftwareVersion",
    0x0752: "CurrentSceneFileEdited",
    0x0753: "MovieRecButtonToggleEnableStatus",
    0x0754: "RemoteTouchOperationEnableStatus",
    0x0755: "CancelRemoteTouchOperationEnableStatus",
    0x0756: "LensInformationEnableStatus",
    0x0757: "FollowFocusPositionCurrentValue",
    0x0758: "FocusBracketShootingStatus",
    0x0759: "PixelMappingEnableStatus",
    0x075A: "TimeCodePresetResetEnableStatus",
    0x075B: "UserBitPresetResetEnableStatus",
    0x075C: "SensorCleaningEnableStatus",
    0x075D: "PictureProfileResetEnableStatus",
    0x075E: "CreativeLookResetEnableStatus",
    0x075F: "LensVersionNumber",
    0x0760: "DeviceOverheatingState",
    0x0761: "Movie_IntervalRec_CountDownIntervalTime",
    0x0762: "Movie_IntervalRec_RecordingDuration",
    0x0763: "HighResolutionShutterSpeed",
    0x0764: "BaseLookImportOperationEnableStatus",
    0x0765: "LensModelName",
    0x0766: "FocusPositionCurrentValue",
    0x0767: "FocusDrivingStatus",
    0x0768: "FlickerScanStatus",
    0x0769: "FlickerScanEnableStatus",
    0x076B: "FTPServerSettingOperationEnableStatus",
    0x076C: "FTPTransferSetting_SaveOperationEnableStatus",
    0x076D: "FTPTransferSetting_ReadOperationEnableStatus",
    0x076E: "FTPTransferSetting_SaveRead_State",
    0x0770: "CameraShakeStatus",
    0x0771: "UpdateBodyStatus",
    0x0773: "MediaSLOT1_WritingState",
    0x0774: "MediaSLOT2_WritingState",
    0x0776: "MediaSLOT1_RecordingAvailableType",
    0x0777: "MediaSLOT2_RecordingAvailableType",
    0x0778: "MediaSLOT3_RecordingAvailableType",
    0x0779: "CameraOperatingMode",
    0x077A: "PlaybackViewMode",
    0x0781: "MediaSLOT3_Status",
    0x0783: "MediaSLOT3_RemainingTime",
    0x0786: "MonitoringDeliveringStatus",
    0x0787: "MonitoringIsDelivering",
    0x0788: "MonitoringSettingVersion",
    0x0789: "MonitoringDeliveryTypeSupportInfo",
    0x078B: "CameraErrorCautionStatus",
    0x078C: "SystemErrorCautionStatus",
    0x078D: "CameraButtonFunctionStatus",
    0x078E: "FlickerLessShootingStatus",
    0x078F: "ContinuousShootingSpotBoostStatus",
    0x0790: "ContinuousShootingSpotBoostEnableStatus",
    0x0791: "TimeShiftShootingStatus",
    0x0792: "ZoomDrivingStatus",
    0x0793: "ShootingSelfTimerStatus",
    0x0794: "CreateNewFolderEnableStatus",
    0x0795: "ForcedFileNumberResetEnableStatus",
    0x0796: "DefaultAFFreeSizeAndPositionSetting",
    0x0797: "TrackingOnAndAFOnEnableStatus",
    0x0798: "ProgramShiftStatus",
    0x0799: "MeteredManualLevel",
    0x079B: "SecondBatteryRemain",
    0x079C: "SecondBatteryLevel",
    0x079D: "TotalBatteryRemain",
    0x079E: "TotalBatteryLevel",
    0x028D: "CameraLeverFunction",
    0x028E: "ShootingTimingPreNotificationMode",
    0x028F: "MicrophoneDirectivity",
    0x0290: "ProductShowcaseSet",
    0x0291: "AmountOfDefocusSetting",
    0x0292: "CinematicVlogSetting",
    0x0293: "CinematicVlogLook",
    0x0294: "CinematicVlogMood",
    0x0295: "CinematicVlogAFTransitionSpeed",
    0x07A2: "MonitoringTransportProtocol",
    0x07A3: "MonitoringAvailableFormat",
    0x07A4: "MonitoringFormatSupportInformation",
    0x02BB: "DeSqueezeDisplayRatio",
    0x02BC: "ZoomPositionSetting",
    0x07A1: "ZoomPositionCurrentValue",
    0x0296: "MonitoringOutputDisplaySDI",
    0x07AC: "CameraSystemErrorInfo",
    0x0297: "AFAreaPositionAF_C",
    0x0298: "AFAreaPositionAF_S",
    0x07AD: "FaceEyeDetectionAFStatus",
    0x0299: "AutoFocusHold",
    0x029A: "PushAFModeSetting",
    0x029B: "TouchFunctionInMF",
    0x029C: "PushAutoFocus",
    0x029D: "PushAGC",
    0x029E: "PushAutoIris",
    0x02A3: "NDFilterPreset3Value",
    0x02A2: "NDFilterPreset2Value",
    0x02A1: "NDFilterPreset1Value",
    0x02A0: "NDFilterPresetSelect",
    0x029F: "PushAutoNDFilter",
    0x02AB: "WhiteBalanceOffsetColorTemp",
    0x02AA: "WhiteBalanceOffsetSetting",
    0x02A9: "WhiteBalanceOffsetTintATW",
    0x02A8: "WhiteBalanceOffsetColorTempATW",
    0x02A7: "WhiteBalanceBGain",
    0x02A6: "WhiteBalanceRGain",
    0x02A5: "WhiteBalancePresetColorTemperature",
    0x02A4: "WhiteBalanceSwitch",
    0x02B4: "PaintLookDetailLevel",
    0x02B3: "PaintLookDetailSetting",
    0x02B2: "PaintLookKneeSlope",
    0x02B1: "PaintLookKneePoint",
    0x02B0: "PaintLookAutoKnee",
    0x02AF: "PaintLookKneeSetting",
    0x02AE: "PaintLookBBlack",
    0x02AD: "PaintLookRBlack",
    0x02AC: "PaintLookMasterBlack",
    0x07AE: "UploadDatasetVersion",
    0x02B5: "UserBaseLookOutput",
    0x07AF: "MonitorLUTSettingOutputDestAssign",
    0x02B6: "MonitorLUTSetting1",
    0x02B7: "MonitorLUTSetting2",
    0x02B8: "MonitorLUTSetting3",
    0x07B0: "MaximumNumberOfBytes",
    0x02B9: "SQModeSetting",
    0x02BA: "MovieQualityFullAutoMode",
    0x02BD: "FileSettingsCameraId",
    0x02BE: "FileSettingsReelNumber",
    0x02BF: "FileSettingsCameraPosition",
    0x02C0: "ImageStabilizationFramingStabilizer",
    0x02C1: "ExposureStep",
    0x07A0: "TeleWideLeverValueCapability",
    0x02C2: "EnlargeScreenSetting",
    0x07A5: "MediaSLOT1_ContentsInfoListEnableStatus",
    0x07A6: "MediaSLOT2_ContentsInfoListEnableStatus",
    0x07A7: "MediaSLOT1_ContentsInfoListRegenerateUpdateTime",
    0x07A8: "MediaSLOT2_ContentsInfoListRegenerateUpdateTime",
    0x07A9: "MediaSLOT1_ContentsInfoListUpdateTime",
    0x07AA: "MediaSLOT2_ContentsInfoListUpdateTime",
    0x07AB: "PostViewTransferResourceStatus",
    0x02C3: "SimulRecSetting",
    0x02C4: "SimulRecSettingMovieRecButton",
    0x02C9: "ShutterSelectMode",
    0x02C5: "OSDImageMode",
    0x07B1: "FirmwareUpdateCommandVersion",
    0x02C6: "DebugMode",
    0x02C7: "reserved18",
    0x02C8: "reserved19",
    0x07B5: "SetPresetPTZFBinaryVersion",
    0x07B6: "PanPositionStatus",
    0x07B7: "TiltPositionStatus",
    0x07B8: "PanPositionCurrentValue",
    0x07B9: "TiltPositionCurrentValue",
    0x02CB: "PanTiltAccelerationRampCurve",
    0x02CC: "PanLimitMode",
    0x02CD: "PanLimitRangeMinimum",
    0x02CE: "PanLimitRangeMaximum",
    0x02CF: "TiltLimitMode",
    0x02D0: "TiltLimitRangeMinimum",
    0x02D1: "TiltLimitRangeMaximum",
    0x02D2: "PresetPTZFSlotNumber",
    0x07BA: "CameraPowerStatus",
    0x0313: "TargetStreamingDestinationSelect",
    0x07CD: "StreamStatus",
    0x02D3: "IRRemoteSetting",
    0x02D4: "IPSetupProtocolSetting",
    0x07BB: "RecordablePowerSources",
    0x07CF: "StreamSettingListOperationStatus",
    0x02E4: "PaintLookMultiMatrixAreaIndication",
    0x02D5: "IrisCloseSetting",
    0x07BC: "DisplayedMenuStatus",
    0x02D6: "LanguageSetting",
    0x07BD: "PlaybackContentsRecordingDateTime",
    0x07BE: "PlaybackContentsName",
    0x07BF: "PlaybackContentsNumber",
    0x07C0: "PlaybackContentsTotalNumber",
    0x07C1: "PlaybackContentsRecordingResolution",
    0x07C2: "PlaybackContentsRecordingFrameRate",
    0x07C3: "PlaybackContentsRecordingFileFormat",
    0x07C4: "PlaybackContentsGammaType",
    0x07C5: "BaseLookNameofPlayback",
    0x07C6: "BaseLookAppliedofPlayback",
    0x02D7: "PaintLookUserMatrixSetting",
    0x02D8: "PaintLookUserMatrixLevel",
    0x02D9: "PaintLookUserMatrixPhase",
    0x02DA: "PaintLookUserMatrixRG",
    0x02DB: "PaintLookUserMatrixRB",
    0x02DC: "PaintLookUserMatrixGR",
    0x02DD: "PaintLookUserMatrixGB",
    0x02DE: "PaintLookUserMatrixBR",
    0x02DF: "PaintLookUserMatrixBG",
    0x02E0: "PaintLookMultiMatrixSetting",
    0x02E1: "PaintLookMultiMatrixAxis",
    0x02E2: "PaintLookMultiMatrixHue",
    0x02E3: "PaintLookMultiMatrixSaturation",
    0x07C7: "MonitoringOutputDisplaySettingDestAssign",
    0x02FC: "MonitoringOutputDisplaySetting1",
    0x02FD: "MonitoringOutputDisplaySetting2",
    0x07C8: "FocusModeStatus",
    0x07C9: "FocusOperationWithInt16EnableStatus",
    0x02E5: "AudioInputCH1LevelControl",
    0x02E6: "AudioInputCH2LevelControl",
    0x02E7: "AudioInputCH3LevelControl",
    0x02E8: "AudioInputCH4LevelControl",
    0x02E9: "AudioInputCH1Level",
    0x02EA: "AudioInputCH2Level",
    0x02EB: "AudioInputCH3Level",
    0x02EC: "AudioInputCH4Level",
    0x02ED: "AudioInputCH1InputSelect",
    0x02EE: "AudioInputCH2InputSelect",
    0x02EF: "AudioInputCH3InputSelect",
    0x02F0: "AudioInputCH4InputSelect",
    0x02F1: "AudioInputCH1WindFilter",
    0x02F2: "AudioInputCH2WindFilter",
    0x02F3: "AudioInputCH3WindFilter",
    0x02F4: "AudioInputCH4WindFilter",
    0x02F7: "RemoteKeyThumbnailButton",
    0x02F8: "RemoteKeySLOTSelectButton",
    0x02F9: "VideoRecordingFormatBitrateSetting",
    0x07CA: "ValidRecordingVideoFormat",
    0x02FB: "MonitoringOutputFormat",
    0x02FE: "FocusSpeedDirectSync",
    0x02F5: "AudioInput1TypeSelect",
    0x02F6: "AudioInput2TypeSelect",
    0x02FA: "VideoRecordingFormatQuality",
    0x02FF: "LiveViewImageQualityByNumericalValue",
    0x0300: "TallyLampControlRed",
    0x0301: "TallyLampControlGreen",
    0x0302: "TallyLampControlYellow",
    0x0305: "Movie_RecordingResolutionForRTSP",
    0x0307: "Movie_RecordingFrameRateRTSPSetting",
    0x0308: "PictureCacheRecSetting",
    0x0309: "PictureCacheRecSizeAndTime",
    0x030A: "Movie_IntervalRecFrames",
    0x030B: "ImagerScanMode",
    0x0306: "Movie_RecordingResolutionForRAW",
    0x07CB: "LensSerialNumber",
    0x030C: "ShootingEnableSettingLicense",
    0x030D: "GridLineDisplayPlayback",
    0x030E: "GridLineType",
    0x07D9: "CustomGridLineFileCommandVersion",
    0x07CC: "MaximumSizeOfImageIDString",
    0x07CE: "StreamButtonEnableStatus",
    0x07B3: "AutoRecognitionTargetCandidates",
    0x02CA: "AutoRecognitionTargetSetting",
    0x07D3: "DeleteContentOperationEnableStatusSLOT1",
    0x07D4: "DeleteContentOperationEnableStatusSLOT2",
    0x030F: "DifferentSetForSQMovie",
    0x0310: "ManualInputForNDFilterValue",
    0x0311: "LogShootingMode",
    0x0312: "LogShootingModeColorGamut",
    0x0315: "VideoStreamSelect",
    0x0314: "StreamDisplayName",
    0x0316: "VideoStreamResolution",
    0x0317: "VideoStreamMaxBitRate",
    0x0318: "VideoStreamAdaptiveRateControl",
    0x0319: "VideoStreamCodec",
    0x031A: "StreamLatency",
    0x031B: "StreamTTL",
    0x031C: "StreamCipherType",
    0x031D: "StreamModeSetting",
    0x031E: "VideoStreamResolutionMethod",
    0x031F: "VideoStreamMovieRecPermission",
    0x0320: "VideoStreamBitRateCompressionMode",
    0x0321: "VideoStreamBitRateVBRMode",
    0x0322: "AudioStreamCodecType",
    0x0323: "AudioStreamSamplingFrequency",
    0x0324: "AudioStreamBitDepth",
    0x0325: "AudioStreamChannel",
    0x0326: "HomeMenuSetting",
    0x0327: "CallSetting",
    0x0328: "NDFilterPositionSetting",
    0x07D5: "SceneFileCommandVersion",
    0x07D6: "SceneFileUploadOperationEnableStatus",
    0x07D7: "SceneFileDownloadOperationEnableStatus",
    0x07D8: "SceneFileIndexesAvailableForDownload",
    0x07D1: "EframingType",
    0x07D2: "EframingCommandVersion",
    0x0329: "EframingAutoFraming",
    0x032A: "EframingTrackingStartMode",
    0x032B: "EframingProductionEffect",
    0x032C: "EframingSpeedPTZ",
    0x0331: "TopOfTheGroupShootingMarkSetting",
    0x0332: "CompRAWShootingNR",
    0x0333: "CompRAWShootingNRFileCompressionType",
    0x0334: "CompRAWShootingNRNumberOfSheets",
    0x07DA: "ElapsedBulbExposureTime",
    0x07DB: "RemainingBulbExposureTime",
    0x07DC: "RemainingNoiseReductionTime",
    0x032D: "DigitalExtenderMagnificationSetting",
    0x032E: "MovieRecReviewPlayingState",
    0x011F: "NearFar",
    0x0120: "reserved7",
    0x0121: "AF_Area_Position",
    0x0126: "Zoom_Operation",
    0x0134: "ZoomAndFocusPosition_Save",
    0x0135: "ZoomAndFocusPosition_Load",
    0x015B: "ColortempStep",
    0x015E: "WhiteBalanceTintStep",
    0x015F: "Focus_Operation",
    0x0162: "ShutterECSNumberStep",
    0x0193: "RemoteTouchOperation",
    0x027C: "ZoomAndFocusPresetZoomOnly_Set",
    0x0509: "CustomWB_Capture_Standby",
    0x050A: "CustomWB_Capture_Standby_Cancel",
    0x050B: "CustomWB_Capture",
    0x0303: "ZoomOperationWithInt16",
    0x0304: "FocusOperationWithInt16",
    0x032F: "HighResolutionShutterSpeedAdjust",
    0x0330: "HighResolutionShutterSpeedAdjustInIntegralMultiples",
    0x034B: "Movie_AngleOfViewPriority",
    0x034C: "WindNoiseReductForExternalMic",
    0x034D: "NoiseCutFilter",
    0x034E: "NoiseCutFilterForExternalMic",
    0x07DD: "DispModeCandidateStill",
    0x0339: "DispModeSettingStill",
    0x033A: "DispModeStill",
    0x07DE: "DispModeCandidateMovie",
    0x033B: "DispModeSettingMovie",
    0x033C: "DispModeMovie",
    0x0335: "CompRAWShootingHDR",
    0x0338: "CompRAWShootingHDRDRSetting",
    0x0336: "CompRAWShootingHDRFileCompressionType",
    0x0337: "CompRAWShootingHDRNumberOfSheets",
    0x07DF: "ControlGeneralSettingFileEnableStatus",
    0x033D: "PeakingDisplay",
    0x033E: "PeakingLevel",
    0x033F: "PeakingColor",
    0x0340: "ZebraDisplay",
    0x0341: "ZebraLevel",
    0x0342: "ZebraLevelTypeCustom",
    0x0343: "ZebraLevelStandardCustom",
    0x0344: "ZebraLevelRangeCustom",
    0x0345: "ZebraLevelLowerLimitCustom",
    0x0346: "MarkerDisplay",
    0x0347: "CenterMarkerDisplay",
    0x0348: "AspectMarkerRatioMovie",
    0x0349: "SafetyZoneDisplay",
    0x034A: "GuideframeDisplay",
    0x034F: "DualGain",
    0x0350: "ImagerMode",
    0x0351: "DisplayQualityForFinderOnly",
    0x0352: "DisplayQualityForMonitorOnly",
}


WIRE_PROPERTY_NAMES = {
    0x5007: "FNumber",
    0x5010: "ExposureBiasCompensation",
    0xD200: "FlashCompensation",
    0xD20D: "ShutterSpeed",
    0xD21E: "IsoSensitivity",
    0x500E: "ExposureProgramMode",
    0xD253: "FileType",
    0xD28B: "MediaSLOT1_FileType",
    0xD28C: "MediaSLOT2_FileType",
    0xD252: "StillImageQuality",
    0xD28D: "MediaSLOT1_ImageQuality",
    0xD28E: "MediaSLOT2_ImageQuality",
    0x5005: "WhiteBalance",
    0x500A: "FocusMode",
    0x500B: "MeteringMode",
    0x500C: "FlashMode",
    0xD262: "WirelessFlash",
    0xD263: "RedEyeReduction",
    0x5013: "DriveMode",
    0xD201: "DRO",
    0xD203: "ImageSize",
    0xD28F: "MediaSLOT1_ImageSize",
    0xD290: "MediaSLOT2_ImageSize",
    0xD211: "AspectRatio",
    0xD21B: "PictureEffect",
    0xD22C: "FocusArea",
    0xD219: "reserved4",
    0xD20F: "Colortemp",
    0xD21C: "ColorTuningAB",
    0xD210: "ColorTuningGM",
    0xD231: "LiveViewDisplayEffect",
    0xD222: "StillImageStoreDestination",
    0xD25A: "PriorityKeySettings",
    0xD255: "AFTrackingSensitivity",
    0xD254: "Focus_Magnifier_Setting",
    0xD223: "DateTime_Settings",
    0xD25C: "Zoom_Scale",
    0xD25F: "Zoom_Setting",
    0xD241: "Movie_File_Format",
    0xD242: "Movie_Recording_Setting",
    0xD286: "Movie_Recording_FrameRateSetting",
    0xD287: "CompressionFileFormatStill",
    0xD288: "RAW_FileCompressionType",
    0xD289: "MediaSLOT1_RAW_FileCompressionType",
    0xD28A: "MediaSLOT2_RAW_FileCompressionType",
    0xD001: "IrisModeSetting",
    0xD013: "ShutterModeSetting",
    0xD01C: "GainControlSetting",
    0xD020: "GainBaseIsoSensitivity",
    0xD021: "GainBaseSensitivity",
    0xD022: "ExposureIndex",
    0xD03C: "BaseLookValue",
    0xD042: "PlaybackMedia",
    0xD045: "DispModeSetting",
    0xD046: "DispMode",
    0xD047: "TouchOperation",
    0xD048: "SelectFinderMonitor",
    0xD049: "AutoPowerOffTemperature",
    0xD04A: "BodyKeyLock",
    0xD092: "ImageID_Num_Setting",
    0xD04B: "ImageID_Num",
    0xD04C: "ImageID_String",
    0xD099: "ExposureCtrlType",
    0xD04D: "MonitorLUTSetting",
    0xD004: "FocalDistanceInMeter",
    0xD005: "FocalDistanceInFeet",
    0xD006: "FocalDistanceUnitSetting",
    0xD00A: "DigitalZoomScale",
    0xD00B: "ZoomDistance",
    0xD029: "ZoomDistanceUnitSetting",
    0xD011: "ShutterModeStatus",
    0xD014: "ShutterSlow",
    0xD015: "ShutterSlowFrames",
    0xD024: "Movie_Recording_ResolutionForMain",
    0xD025: "Movie_Recording_ResolutionForProxy",
    0xD028: "Movie_Recording_FrameRateProxySetting",
    0xD037: "BatteryRemainDisplayUnit",
    0xD03A: "PowerSource",
    0xE000: "MovieShootingMode",
    0xE001: "MovieShootingModeColorGamut",
    0xE002: "MovieShootingModeTargetDisplay",
    0xE009: "DepthOfFieldAdjustmentMode",
    0xD00C: "WhiteBalanceModeSetting",
    0xD00D: "WhiteBalanceTint",
    0xE006: "ShutterECSSetting",
    0xE007: "ShutterECSNumber",
    0xE008: "ShutterECSFrequency",
    0xE00D: "RecorderControlProxySetting",
    0xE014: "ButtonAssignmentAssignable1",
    0xE015: "ButtonAssignmentAssignable2",
    0xE016: "ButtonAssignmentAssignable3",
    0xE017: "ButtonAssignmentAssignable4",
    0xE018: "ButtonAssignmentAssignable5",
    0xE019: "ButtonAssignmentAssignable6",
    0xE01A: "ButtonAssignmentAssignable7",
    0xE01B: "ButtonAssignmentAssignable8",
    0xE01C: "ButtonAssignmentAssignable9",
    0xE01D: "ButtonAssignmentAssignable10",
    0xE08D: "ButtonAssignmentAssignable11",
    0xE01E: "ButtonAssignmentLensAssignable1",
    0xE029: "AssignableButton1",
    0xE02A: "AssignableButton2",
    0xE02B: "AssignableButton3",
    0xE02C: "AssignableButton4",
    0xE02D: "AssignableButton5",
    0xE02E: "AssignableButton6",
    0xE02F: "AssignableButton7",
    0xE030: "AssignableButton8",
    0xE031: "AssignableButton9",
    0xE032: "AssignableButton10",
    0xE08E: "AssignableButton11",
    0xE033: "LensAssignableButton1",
    0xD007: "FocusModeSetting",
    0xD00E: "ShutterAngle",
    0xD00F: "ShutterSetting",
    0xD010: "ShutterMode",
    0xD016: "ShutterSpeedValue",
    0xD018: "NDFilter",
    0xD01A: "NDFilterModeSetting",
    0xD01B: "NDFilterValue",
    0xD01D: "GainUnitSetting",
    0xD01E: "GaindBValue",
    0xD03B: "AWB",
    0xE01F: "SceneFileIndex",
    0xE021: "MoviePlayButton",
    0xE022: "MoviePlayPauseButton",
    0xE023: "MoviePlayStopButton",
    0xE024: "MovieForwardButton",
    0xE025: "MovieRewindButton",
    0xE026: "MovieNextButton",
    0xE027: "MoviePrevButton",
    0xE028: "MovieRecReviewButton",
    0xD060: "SubjectRecognitionAF",
    0xD061: "AFTransitionSpeed",
    0xD062: "AFSubjShiftSens",
    0xE084: "AFAssist",
    0xD073: "NDFilterSwitchingSetting",
    0xE083: "FunctionOfRemoteTouchOperation",
    0xE088: "FollowFocusPositionSetting",
    0xD2A1: "FocusBracketShotNumber",
    0xD2A2: "FocusBracketFocusRange",
    0xD0C5: "ExtendedInterfaceMode",
    0xD0D0: "SQRecordingFrameRateSetting",
    0xD052: "SQFrameRate",
    0xD0D1: "SQRecordingSetting",
    0xD0D2: "AudioRecording",
    0xE050: "AudioInputMasterLevel",
    0xD0D3: "TimeCodePreset",
    0xD0D5: "TimeCodeFormat",
    0xD0D6: "TimeCodeRun",
    0xD0D7: "TimeCodeMake",
    0xD0D4: "UserBitPreset",
    0xD0D8: "UserBitTimeRec",
    0xD0D9: "ImageStabilizationSteadyShot",
    0xD0DA: "Movie_ImageStabilizationSteadyShot",
    0xD0DB: "SilentMode",
    0xD0DC: "SilentModeApertureDriveInAF",
    0xD0DD: "SilentModeShutterWhenPowerOff",
    0xD0DE: "SilentModeAutoPixelMapping",
    0xD0DF: "ShutterType",
    0xD23F: "PictureProfile",
    0xD0E0: "PictureProfile_BlackLevel",
    0xD0E1: "PictureProfile_Gamma",
    0xD0E2: "PictureProfile_BlackGammaRange",
    0xD0E3: "PictureProfile_BlackGammaLevel",
    0xD0E4: "PictureProfile_KneeMode",
    0xD0E5: "PictureProfile_KneeAutoSet_MaxPoint",
    0xD0E6: "PictureProfile_KneeAutoSet_Sensitivity",
    0xD0E7: "PictureProfile_KneeManualSet_Point",
    0xD0E8: "PictureProfile_KneeManualSet_Slope",
    0xD0E9: "PictureProfile_ColorMode",
    0xD0EA: "PictureProfile_Saturation",
    0xD0EB: "PictureProfile_ColorPhase",
    0xD0EC: "PictureProfile_ColorDepthRed",
    0xD0ED: "PictureProfile_ColorDepthGreen",
    0xD0EE: "PictureProfile_ColorDepthBlue",
    0xD0EF: "PictureProfile_ColorDepthCyan",
    0xD0F0: "PictureProfile_ColorDepthMagenta",
    0xD0F1: "PictureProfile_ColorDepthYellow",
    0xD0F2: "PictureProfile_DetailLevel",
    0xD0F3: "PictureProfile_DetailAdjustMode",
    0xD0F4: "PictureProfile_DetailAdjustVHBalance",
    0xD0F5: "PictureProfile_DetailAdjustBWBalance",
    0xD0F6: "PictureProfile_DetailAdjustLimit",
    0xD0F7: "PictureProfile_DetailAdjustCrispening",
    0xD0F8: "PictureProfile_DetailAdjustHiLightDetail",
    0xD0F9: "PictureProfile_Copy",
    0xD0FA: "CreativeLook",
    0xD0FB: "CreativeLook_Contrast",
    0xD0FC: "CreativeLook_Highlights",
    0xD0FD: "CreativeLook_Shadows",
    0xD0FE: "CreativeLook_Fade",
    0xD0FF: "CreativeLook_Saturation",
    0xD100: "CreativeLook_Sharpness",
    0xD101: "CreativeLook_SharpnessRange",
    0xD102: "CreativeLook_Clarity",
    0xD103: "CreativeLook_CustomLook",
    0xD027: "Movie_ProxyFileFormat",
    0xD109: "ProxyRecordingSetting",
    0xD283: "FunctionOfTouchOperation",
    0xD281: "HighResolutionShutterSpeedSetting",
    0xD0C7: "DeleteUserBaseLook",
    0xD0C8: "SelectUserBaseLookToEdit",
    0xD0CC: "SelectUserBaseLookToSetInPPLUT",
    0xD0C9: "UserBaseLookInput",
    0xD0CA: "UserBaseLookAELevelOffset",
    0xD0CB: "BaseISOSwitchEI",
    0xD133: "FlickerLessShooting",
    0xD172: "AudioLevelDisplay",
    0xD17C: "PlaybackVolumeSettings",
    0xD17D: "AutoReview",
    0xD17E: "AudioSignals",
    0xD17F: "HDMIResolutionStillPlay",
    0xD180: "Movie_HDMIOutputRecMedia",
    0xD181: "Movie_HDMIOutputResolution",
    0xD182: "Movie_HDMIOutput4KSetting",
    0xD183: "Movie_HDMIOutputRAW",
    0xD184: "Movie_HDMIOutputRawSetting",
    0xD185: "Movie_HDMIOutputColorGamutForRAWOut",
    0xD186: "Movie_HDMIOutputTimeCode",
    0xD187: "Movie_HDMIOutputRecControl",
    0xD079: "MonitoringOutputDisplayHDMI",
    0xE059: "Movie_HDMIOutputAudioCH",
    0xD055: "Movie_IntervalRec_IntervalTime",
    0xD151: "Movie_IntervalRec_FrameRateSetting",
    0xD152: "Movie_IntervalRec_RecordingSetting",
    0xD0CD: "EframingScaleAuto",
    0xD0CE: "EframingSpeedAuto",
    0xD124: "EframingModeAuto",
    0xD153: "EframingRecordingImageCrop",
    0xD154: "EframingHDMICrop",
    0xD0CF: "CameraEframing",
    0xD150: "USBPowerSupply",
    0xD15B: "LongExposureNR",
    0xD15C: "HighIsoNR",
    0xD15D: "HLGStillImage",
    0xD15E: "ColorSpace",
    0xD166: "BracketOrder",
    0xD167: "FocusBracketOrder",
    0xD168: "FocusBracketExposureLock1stImg",
    0xD169: "FocusBracketIntervalUntilNextShot",
    0xD16A: "IntervalRec_ShootingStartTime",
    0xD16B: "IntervalRec_ShootingInterval",
    0xD16F: "IntervalRec_ShootIntervalPriority",
    0xD16C: "IntervalRec_NumberOfShots",
    0xD16D: "IntervalRec_AETrackingSensitivity",
    0xD16E: "IntervalRec_ShutterType",
    0xD170: "ElectricFrontCurtainShutter",
    0xD171: "WindNoiseReduct",
    0xD29C: "RecordingSelfTimer",
    0xD29D: "RecordingSelfTimerCountTime",
    0xD29F: "RecordingSelfTimerContinuous",
    0xD2A0: "RecordingSelfTimerStatus",
    0xD2A4: "BulbTimerSetting",
    0xD2A5: "BulbExposureTimeSetting",
    0xD173: "AutoSlowShutter",
    0xD14D: "IsoAutoMinShutterSpeedMode",
    0xD176: "IsoAutoMinShutterSpeedManual",
    0xD177: "IsoAutoMinShutterSpeedPreset",
    0xE042: "FocusPositionSetting",
    0xD178: "SoftSkinEffect",
    0xD179: "PrioritySetInAF_S",
    0xD17A: "PrioritySetInAF_C",
    0xD17B: "FocusMagnificationTime",
    0xD157: "SubjectRecognitionInAF",
    0xD158: "RecognitionTarget",
    0xD159: "RightLeftEyeSelect",
    0xD27C: "SelectFTPServer",
    0xD02E: "SelectFTPServerID",
    0xD041: "FTP_Function",
    0xD04E: "FTP_AutoTransfer",
    0xD04F: "FTP_AutoTransferTarget",
    0xD199: "Movie_FTP_AutoTransferTarget",
    0xD19A: "FTP_TransferTarget",
    0xD14B: "Movie_FTP_TransferTarget",
    0xD14C: "FTP_PowerSave",
    0xD14E: "NDFilterUnitSetting",
    0xD14F: "NDFilterOpticalDensityValue",
    0xD000: "TNumber",
    0xD003: "IrisDisplayUnit",
    0xE080: "Movie_ImageStabilizationLevel",
    0xD192: "ImageStabilizationSteadyShotAdjust",
    0xD193: "ImageStabilizationSteadyShotFocalLength",
    0xD19F: "ExtendedShutterSpeed",
    0xD208: "CameraButtonFunction",
    0xD209: "CameraButtonFunctionMulti",
    0xD20A: "CameraDialFunction",
    0xD155: "SynchroterminalForcedOutput",
    0xD156: "ShutterReleaseTimeLagControl",
    0xD12F: "ContinuousShootingSpotBoostFrameSpeed",
    0xD189: "TimeShiftShooting",
    0xD18A: "TimeShiftTriggerSetting",
    0xD18B: "TimeShiftPreShootingTimeSetting",
    0xD196: "EmbedLUTFile",
    0xD1C7: "APS_C_S35",
    0xD1A2: "LensCompensationShading",
    0xD1A3: "LensCompensationChromaticAberration",
    0xD1A4: "LensCompensationDistortion",
    0xD1A5: "LensCompensationBreathing",
    0xD15F: "RecordingMedia",
    0xD160: "Movie_RecordingMedia",
    0xD161: "AutoSwitchMedia",
    0xD1C8: "RecordingFileNumber",
    0xD2B5: "Movie_RecordingFileNumber",
    0xD1CA: "RecordingSettingFileName",
    0xD1CB: "RecordingFolderFormat",
    0xD132: "SelectIPTCMetadata",
    0xD1CD: "WriteCopyrightInfo",
    0xD1CE: "SetPhotographer",
    0xD1CF: "SetCopyright",
    0xD1DC: "FileSettingsTitleNameSettings",
    0xD1A6: "FocusBracketRecordingFolder",
    0xD1A7: "ReleaseWithoutLens",
    0xD1A8: "ReleaseWithoutCard",
    0xD1DE: "GridLineDisplay",
    0xD162: "ContinuousShootingSpeedInElectricShutterHiPlus",
    0xD163: "ContinuousShootingSpeedInElectricShutterHi",
    0xD164: "ContinuousShootingSpeedInElectricShutterMid",
    0xD165: "ContinuousShootingSpeedInElectricShutterLo",
    0xD1B6: "IsoAutoRangeLimitMin",
    0xD1B7: "IsoAutoRangeLimitMax",
    0xD1E5: "FacePriorityInMultiMetering",
    0xD1AA: "PrioritySetInAWB",
    0xD135: "CustomWB_Size_Setting",
    0xD1AB: "AFIlluminator",
    0xD1AC: "ApertureDriveInAF",
    0xD1AD: "AFWithShutter",
    0xD1AE: "FullTimeDMF",
    0xD1AF: "PreAF",
    0xD1E6: "SubjectRecognitionPersonTrackingSubjectShiftRange",
    0xD1E7: "SubjectRecognitionAnimalBirdPriority",
    0xD1E8: "SubjectRecognitionAnimalBirdDetectionParts",
    0xD1E9: "SubjectRecognitionAnimalTrackingSubjectShiftRange",
    0xD1EA: "SubjectRecognitionAnimalTrackingSensitivity",
    0xD1EB: "SubjectRecognitionAnimalDetectionSensitivity",
    0xD1EC: "SubjectRecognitionAnimalDetectionParts",
    0xD1ED: "SubjectRecognitionBirdTrackingSubjectShiftRange",
    0xD1EE: "SubjectRecognitionBirdTrackingSensitivity",
    0xD1EF: "SubjectRecognitionBirdDetectionSensitivity",
    0xD1F0: "SubjectRecognitionBirdDetectionParts",
    0xD1F1: "SubjectRecognitionInsectTrackingSubjectShiftRange",
    0xD1F2: "SubjectRecognitionInsectTrackingSensitivity",
    0xD1F3: "SubjectRecognitionInsectDetectionSensitivity",
    0xD1F4: "SubjectRecognitionCarTrainTrackingSubjectShiftRange",
    0xD1F5: "SubjectRecognitionCarTrainTrackingSensitivity",
    0xD1F6: "SubjectRecognitionCarTrainDetectionSensitivity",
    0xD1F7: "SubjectRecognitionPlaneTrackingSubjectShiftRange",
    0xD1F8: "SubjectRecognitionPlaneTrackingSensitivity",
    0xD1F9: "SubjectRecognitionPlaneDetectionSensitivity",
    0xD1FA: "SubjectRecognitionPriorityOnRegisteredFace",
    0xD1B8: "FaceEyeFrameDisplay",
    0xD1B9: "FocusMap",
    0xD1BD: "InitialFocusMagnifier",
    0xD1BA: "AFInFocusMagnifier",
    0xD2AD: "AFTrackForSpeedChange",
    0xD138: "AFFreeSizeAndPositionSetting",
    0xD2B2: "PlaySetOfMultiMedia",
    0xD1BE: "RemoteSaveImageSize",
    0xD14A: "FTP_TransferStillImageQualitySize",
    0xD216: "FTP_AutoTransferTarget_StillImage",
    0xD225: "ProtectImageInFTPTransfer",
    0xD1FB: "MonitorBrightnessType",
    0xD1FC: "MonitorBrightnessManual",
    0xD1B0: "DisplayQualityFinderMonitor",
    0xD1FD: "TCUBDisplaySetting",
    0xD1FE: "GammaDisplayAssist",
    0xD1FF: "GammaDisplayAssistType",
    0xD220: "AudioSignalsStartEnd",
    0xD1B1: "AudioSignalsVolume",
    0xD1B2: "ControlForHDMI",
    0xD1B3: "AntidustShutterWhenPowerOff",
    0xD1C1: "WakeOnLAN",
    0xD239: "reserved10",
    0xD23A: "reserved11",
    0xD23B: "reserved12",
    0xD24F: "Interval_Rec_Mode",
    0xD268: "Still_Image_Trans_Size",
    0xD269: "RAW_J_PC_Save_Image",
    0xD26A: "LiveView_Image_Quality",
    0xD299: "Remocon_Zoom_Speed_Type",
    0xD215: "SnapshotInfo",
    0xD218: "BatteryRemain",
    0xD20E: "BatteryLevel",
    0xD214: "EstimatePictureSize",
    0xD21D: "RecordingState",
    0xD221: "LiveViewStatus",
    0xD213: "FocusIndication",
    0xD248: "MediaSLOT1_Status",
    0xD249: "MediaSLOT1_RemainingNumber",
    0xD24A: "MediaSLOT1_RemainingTime",
    0xD279: "MediaSLOT1_FormatEnableStatus",
    0xD27D: "reserved20",
    0xD256: "MediaSLOT2_Status",
    0xD27A: "MediaSLOT2_FormatEnableStatus",
    0xD257: "MediaSLOT2_RemainingNumber",
    0xD258: "MediaSLOT2_RemainingTime",
    0xD27E: "reserved22",
    0xD27B: "Media_FormatProgressRate",
    0xD27F: "FTP_ConnectionStatus",
    0xD280: "FTP_ConnectionErrorInfo",
    0xD267: "LiveView_Area",
    0xD23C: "reserved26",
    0xD23D: "reserved27",
    0xD250: "Interval_Rec_Status",
    0xD270: "CustomWB_Execution_State",
    0xD26B: "CustomWB_Capturable_Area",
    0xD26C: "CustomWB_Capture_Frame_Size",
    0xD26F: "CustomWB_Capture_Operation",
    0xD25B: "Zoom_Operation_Status",
    0xD25D: "Zoom_Bar_Information",
    0xD260: "Zoom_Type_Status",
    0xD292: "MediaSLOT1_QuickFormatEnableStatus",
    0xD293: "MediaSLOT2_QuickFormatEnableStatus",
    0xD294: "Cancel_Media_FormatEnableStatus",
    0xD25E: "Zoom_Speed_Range",
    0xD023: "IsoCurrentSensitivity",
    0xD271: "CameraSetting_SaveOperationEnableStatus",
    0xD272: "CameraSetting_ReadOperationEnableStatus",
    0xD273: "CameraSetting_SaveRead_State",
    0xD043: "CameraSettingsResetEnableStatus",
    0xD29A: "APS_C_or_Full_SwitchingSetting",
    0xD29B: "APS_C_or_Full_SwitchingEnableStatus",
    0xD044: "DispModeCandidate",
    0xD017: "ShutterSpeedCurrentValue",
    0xD008: "Focus_Speed_Range",
    0xD019: "NDFilterMode",
    0xD030: "MoviePlayingSpeed",
    0xD035: "MediaSLOT1Player",
    0xD036: "MediaSLOT2Player",
    0xD038: "BatteryRemainingInMinutes",
    0xD039: "BatteryRemainingInVoltage",
    0xD03E: "DCVoltage",
    0xD02F: "MoviePlayingState",
    0xE004: "FocusTouchSpotStatus",
    0xE005: "FocusTrackingStatus",
    0xE00A: "DepthOfFieldAdjustmentInterlockingMode",
    0xE00B: "RecorderClipName",
    0xE00C: "RecorderControlMainSetting",
    0xE00E: "RecorderStartMain",
    0xE00F: "RecorderStartProxy",
    0xE010: "RecorderMainStatus",
    0xE011: "RecorderProxyStatus",
    0xE012: "RecorderExtRawStatus",
    0xE013: "RecorderSaveDestination",
    0xE035: "AssignableButtonIndicator1",
    0xE036: "AssignableButtonIndicator2",
    0xE037: "AssignableButtonIndicator3",
    0xE038: "AssignableButtonIndicator4",
    0xE039: "AssignableButtonIndicator5",
    0xE03A: "AssignableButtonIndicator6",
    0xE03B: "AssignableButtonIndicator7",
    0xE03C: "AssignableButtonIndicator8",
    0xE03D: "AssignableButtonIndicator9",
    0xE03E: "AssignableButtonIndicator10",
    0xE08F: "AssignableButtonIndicator11",
    0xE03F: "LensAssignableButtonIndicator1",
    0xD01F: "GaindBCurrentValue",
    0xD040: "SoftwareVersion",
    0xE020: "CurrentSceneFileEdited",
    0xE061: "MovieRecButtonToggleEnableStatus",
    0xD284: "RemoteTouchOperationEnableStatus",
    0xD285: "CancelRemoteTouchOperationEnableStatus",
    0xE086: "LensInformationEnableStatus",
    0xE089: "FollowFocusPositionCurrentValue",
    0xD0AB: "FocusBracketShootingStatus",
    0xD0C6: "PixelMappingEnableStatus",
    0xD104: "TimeCodePresetResetEnableStatus",
    0xD105: "UserBitPresetResetEnableStatus",
    0xD106: "SensorCleaningEnableStatus",
    0xD107: "PictureProfileResetEnableStatus",
    0xD108: "CreativeLookResetEnableStatus",
    0xD07D: "LensVersionNumber",
    0xD251: "DeviceOverheatingState",
    0xD11F: "Movie_IntervalRec_CountDownIntervalTime",
    0xD120: "Movie_IntervalRec_RecordingDuration",
    0xD282: "HighResolutionShutterSpeed",
    0xD08B: "BaseLookImportOperationEnableStatus",
    0xD07B: "LensModelName",
    0xE043: "FocusPositionCurrentValue",
    0xD19C: "FocusDrivingStatus",
    0xD2BA: "FlickerScanStatus",
    0xD2BB: "FlickerScanEnableStatus",
    0xD09A: "FTPServerSettingOperationEnableStatus",
    0xD274: "FTPTransferSetting_SaveOperationEnableStatus",
    0xD275: "FTPTransferSetting_ReadOperationEnableStatus",
    0xD276: "FTPTransferSetting_SaveRead_State",
    0xD194: "CameraShakeStatus",
    0xD195: "UpdateBodyStatus",
    0xD197: "MediaSLOT1_WritingState",
    0xD198: "MediaSLOT2_WritingState",
    0xD02B: "MediaSLOT1_RecordingAvailableType",
    0xD02C: "MediaSLOT2_RecordingAvailableType",
    0xD190: "MediaSLOT3_RecordingAvailableType",
    0xD0BC: "CameraOperatingMode",
    0xD0BD: "PlaybackViewMode",
    0xD18E: "MediaSLOT3_Status",
    0xD18F: "MediaSLOT3_RemainingTime",
    0xE098: "MonitoringDeliveringStatus",
    0xE099: "MonitoringIsDelivering",
    0xE09D: "MonitoringSettingVersion",
    0xE09F: "MonitoringDeliveryTypeSupportInfo",
    0xD1BB: "CameraErrorCautionStatus",
    0xD1BC: "SystemErrorCautionStatus",
    0xD20C: "CameraButtonFunctionStatus",
    0xD134: "FlickerLessShootingStatus",
    0xD130: "ContinuousShootingSpotBoostStatus",
    0xD131: "ContinuousShootingSpotBoostEnableStatus",
    0xD19B: "TimeShiftShootingStatus",
    0xD19D: "ZoomDrivingStatus",
    0xD1B4: "ShootingSelfTimerStatus",
    0xD1DB: "CreateNewFolderEnableStatus",
    0xD1C9: "ForcedFileNumberResetEnableStatus",
    0xD19E: "DefaultAFFreeSizeAndPositionSetting",
    0xD1C6: "TrackingOnAndAFOnEnableStatus",
    0xD1BF: "ProgramShiftStatus",
    0xD1B5: "MeteredManualLevel",
    0xD12D: "SecondBatteryRemain",
    0xD12E: "SecondBatteryLevel",
    0xD204: "TotalBatteryRemain",
    0xD205: "TotalBatteryLevel",
    0xD20B: "CameraLeverFunction",
    0xD202: "ShootingTimingPreNotificationMode",
    0xD1DD: "MicrophoneDirectivity",
    0xD1DF: "ProductShowcaseSet",
    0xD1E0: "AmountOfDefocusSetting",
    0xD1E1: "CinematicVlogSetting",
    0xD1E2: "CinematicVlogLook",
    0xD1E3: "CinematicVlogMood",
    0xD1E4: "CinematicVlogAFTransitionSpeed",
    0xE0A1: "MonitoringTransportProtocol",
    0xE0A2: "MonitoringAvailableFormat",
    0xE0A3: "MonitoringFormatSupportInformation",
    0xE0A4: "DeSqueezeDisplayRatio",
    0xE040: "ZoomPositionSetting",
    0xE041: "ZoomPositionCurrentValue",
    0xD078: "MonitoringOutputDisplaySDI",
    0xD07A: "CameraSystemErrorInfo",
    0xE079: "AFAreaPositionAF_C",
    0xE078: "AFAreaPositionAF_S",
    0xD09B: "FaceEyeDetectionAFStatus",
    0xD091: "AutoFocusHold",
    0xD06E: "PushAFModeSetting",
    0xD064: "TouchFunctionInMF",
    0xD05E: "PushAutoFocus",
    0xD05C: "PushAGC",
    0xD05B: "PushAutoIris",
    0xD077: "NDFilterPreset3Value",
    0xD076: "NDFilterPreset2Value",
    0xD075: "NDFilterPreset1Value",
    0xD074: "NDFilterPresetSelect",
    0xD05D: "PushAutoNDFilter",
    0xD0AA: "WhiteBalanceOffsetColorTemp",
    0xD0A9: "WhiteBalanceOffsetSetting",
    0xD08A: "WhiteBalanceOffsetTintATW",
    0xD089: "WhiteBalanceOffsetColorTempATW",
    0xD088: "WhiteBalanceBGain",
    0xD087: "WhiteBalanceRGain",
    0xD086: "WhiteBalancePresetColorTemperature",
    0xD085: "WhiteBalanceSwitch",
    0xD06D: "PaintLookDetailLevel",
    0xD06C: "PaintLookDetailSetting",
    0xD06B: "PaintLookKneeSlope",
    0xD06A: "PaintLookKneePoint",
    0xD069: "PaintLookAutoKnee",
    0xD068: "PaintLookKneeSetting",
    0xD067: "PaintLookBBlack",
    0xD066: "PaintLookRBlack",
    0xD065: "PaintLookMasterBlack",
    0xD057: "UploadDatasetVersion",
    0xD2B1: "UserBaseLookOutput",
    0xD2A9: "MonitorLUTSettingOutputDestAssign",
    0xD2AA: "MonitorLUTSetting1",
    0xD2AB: "MonitorLUTSetting2",
    0xD2AC: "MonitorLUTSetting3",
    0xD0C1: "MaximumNumberOfBytes",
    0xD051: "SQModeSetting",
    0xE0A0: "MovieQualityFullAutoMode",
    0xD1D0: "FileSettingsCameraId",
    0xD1D1: "FileSettingsReelNumber",
    0xD1D2: "FileSettingsCameraPosition",
    0xD1A9: "ImageStabilizationFramingStabilizer",
    0xD237: "ExposureStep",
    0xD2BD: "TeleWideLeverValueCapability",
    0xE0CD: "EnlargeScreenSetting",
    0xD1D4: "MediaSLOT1_ContentsInfoListEnableStatus",
    0xD1D5: "MediaSLOT2_ContentsInfoListEnableStatus",
    0xD1D6: "MediaSLOT1_ContentsInfoListRegenerateUpdateTime",
    0xD1D7: "MediaSLOT2_ContentsInfoListRegenerateUpdateTime",
    0xE0D9: "MediaSLOT1_ContentsInfoListUpdateTime",
    0xE0DA: "MediaSLOT2_ContentsInfoListUpdateTime",
    0xD1DA: "PostViewTransferResourceStatus",
    0xD050: "SimulRecSetting",
    0xD07F: "SimulRecSettingMovieRecButton",
    0xD012: "ShutterSelectMode",
    0xD207: "OSDImageMode",
    0xD0BF: "FirmwareUpdateCommandVersion",
    0xE0D5: "DebugMode",
    0xE0DF: "reserved18",
    0xE0E0: "reserved19",
    0xE0CC: "SetPresetPTZFBinaryVersion",
    0xE0B7: "PanPositionStatus",
    0xE0B9: "TiltPositionStatus",
    0xE0B6: "PanPositionCurrentValue",
    0xE0B8: "TiltPositionCurrentValue",
    0xE05C: "PanTiltAccelerationRampCurve",
    0xE0BE: "PanLimitMode",
    0xE0BA: "PanLimitRangeMinimum",
    0xE0BB: "PanLimitRangeMaximum",
    0xE0BF: "TiltLimitMode",
    0xE0BC: "TiltLimitRangeMinimum",
    0xE0BD: "TiltLimitRangeMaximum",
    0xE0CB: "PresetPTZFSlotNumber",
    0xE0AF: "CameraPowerStatus",
    0xD2BE: "TargetStreamingDestinationSelect",
    0xD119: "StreamStatus",
    0xE0A5: "IRRemoteSetting",
    0xE0A6: "IPSetupProtocolSetting",
    0xE0B0: "RecordablePowerSources",
    0xD1CC: "StreamSettingListOperationStatus",
    0xD29E: "PaintLookMultiMatrixAreaIndication",
    0xD002: "IrisCloseSetting",
    0xD080: "DisplayedMenuStatus",
    0xD08F: "LanguageSetting",
    0xD09C: "PlaybackContentsRecordingDateTime",
    0xD09D: "PlaybackContentsName",
    0xD09E: "PlaybackContentsNumber",
    0xD09F: "PlaybackContentsTotalNumber",
    0xD0A0: "PlaybackContentsRecordingResolution",
    0xD0A1: "PlaybackContentsRecordingFrameRate",
    0xD0A2: "PlaybackContentsRecordingFileFormat",
    0xD0A4: "PlaybackContentsGammaType",
    0xD0C3: "BaseLookNameofPlayback",
    0xD0C4: "BaseLookAppliedofPlayback",
    0xD139: "PaintLookUserMatrixSetting",
    0xD13A: "PaintLookUserMatrixLevel",
    0xD13B: "PaintLookUserMatrixPhase",
    0xD13C: "PaintLookUserMatrixRG",
    0xD13D: "PaintLookUserMatrixRB",
    0xD13E: "PaintLookUserMatrixGR",
    0xD13F: "PaintLookUserMatrixGB",
    0xD140: "PaintLookUserMatrixBR",
    0xD141: "PaintLookUserMatrixBG",
    0xD142: "PaintLookMultiMatrixSetting",
    0xD143: "PaintLookMultiMatrixAxis",
    0xD144: "PaintLookMultiMatrixHue",
    0xD145: "PaintLookMultiMatrixSaturation",
    0xD2AE: "MonitoringOutputDisplaySettingDestAssign",
    0xD2AF: "MonitoringOutputDisplaySetting1",
    0xD2B0: "MonitoringOutputDisplaySetting2",
    0xE044: "FocusModeStatus",
    0xE045: "FocusOperationWithInt16EnableStatus",
    0xE048: "AudioInputCH1LevelControl",
    0xE049: "AudioInputCH2LevelControl",
    0xE04A: "AudioInputCH3LevelControl",
    0xE04B: "AudioInputCH4LevelControl",
    0xE04C: "AudioInputCH1Level",
    0xE04D: "AudioInputCH2Level",
    0xE04E: "AudioInputCH3Level",
    0xE04F: "AudioInputCH4Level",
    0xE051: "AudioInputCH1InputSelect",
    0xE052: "AudioInputCH2InputSelect",
    0xE053: "AudioInputCH3InputSelect",
    0xE054: "AudioInputCH4InputSelect",
    0xE055: "AudioInputCH1WindFilter",
    0xE056: "AudioInputCH2WindFilter",
    0xE057: "AudioInputCH3WindFilter",
    0xE058: "AudioInputCH4WindFilter",
    0xE05F: "RemoteKeyThumbnailButton",
    0xE060: "RemoteKeySLOTSelectButton",
    0xE067: "VideoRecordingFormatBitrateSetting",
    0xE068: "ValidRecordingVideoFormat",
    0xE06C: "MonitoringOutputFormat",
    0xE092: "FocusSpeedDirectSync",
    0xE0AA: "AudioInput1TypeSelect",
    0xE0AB: "AudioInput2TypeSelect",
    0xE0B5: "VideoRecordingFormatQuality",
    0xE0CE: "LiveViewImageQualityByNumericalValue",
    0xE0D2: "TallyLampControlRed",
    0xE0D3: "TallyLampControlGreen",
    0xE0D4: "TallyLampControlYellow",
    0xD026: "Movie_RecordingResolutionForRTSP",
    0xD02D: "Movie_RecordingFrameRateRTSPSetting",
    0xD053: "PictureCacheRecSetting",
    0xD054: "PictureCacheRecSizeAndTime",
    0xD056: "Movie_IntervalRecFrames",
    0xD05F: "ImagerScanMode",
    0xD063: "Movie_RecordingResolutionForRAW",
    0xD07C: "LensSerialNumber",
    0xE0FA: "ShootingEnableSettingLicense",
    0xE10E: "GridLineDisplayPlayback",
    0xE10F: "GridLineType",
    0xE110: "CustomGridLineFileCommandVersion",
    0xE0FE: "MaximumSizeOfImageIDString",
    0xE112: "StreamButtonEnableStatus",
    0xD229: "AutoRecognitionTargetCandidates",
    0xD234: "AutoRecognitionTargetSetting",
    0xE0F3: "DeleteContentOperationEnableStatusSLOT1",
    0xE0F4: "DeleteContentOperationEnableStatusSLOT2",
    0xE0F5: "DifferentSetForSQMovie",
    0xE0E2: "ManualInputForNDFilterValue",
    0xE0E3: "LogShootingMode",
    0xE0E4: "LogShootingModeColorGamut",
    0xD0AC: "VideoStreamSelect",
    0xD2BF: "StreamDisplayName",
    0xD0AE: "VideoStreamResolution",
    0xD2C0: "VideoStreamMaxBitRate",
    0xD10E: "VideoStreamAdaptiveRateControl",
    0xD0AD: "VideoStreamCodec",
    0xD116: "StreamLatency",
    0xD117: "StreamTTL",
    0xD113: "StreamCipherType",
    0xD118: "StreamModeSetting",
    0xD10F: "VideoStreamResolutionMethod",
    0xD11A: "VideoStreamMovieRecPermission",
    0xD0B5: "VideoStreamBitRateCompressionMode",
    0xD2B3: "VideoStreamBitRateVBRMode",
    0xD11B: "AudioStreamCodecType",
    0xD11C: "AudioStreamSamplingFrequency",
    0xD11D: "AudioStreamBitDepth",
    0xD11E: "AudioStreamChannel",
    0xE111: "HomeMenuSetting",
    0xE0E1: "CallSetting",
    0xE0E5: "NDFilterPositionSetting",
    0xE0E6: "SceneFileCommandVersion",
    0xE101: "SceneFileUploadOperationEnableStatus",
    0xE102: "SceneFileDownloadOperationEnableStatus",
    0xE0F9: "SceneFileIndexesAvailableForDownload",
    0xD122: "EframingType",
    0xD123: "EframingCommandVersion",
    0xE0F8: "EframingAutoFraming",
    0xE0F0: "EframingTrackingStartMode",
    0xE0F1: "EframingProductionEffect",
    0xD127: "EframingSpeedPTZ",
    0xD18C: "TopOfTheGroupShootingMarkSetting",
    0xD148: "CompRAWShootingNR",
    0xD149: "CompRAWShootingNRFileCompressionType",
    0xD15A: "CompRAWShootingNRNumberOfSheets",
    0xD2A6: "ElapsedBulbExposureTime",
    0xD2A7: "RemainingBulbExposureTime",
    0xD2A8: "RemainingNoiseReductionTime",
    0xE100: "DigitalExtenderMagnificationSetting",
    0xE07A: "MovieRecReviewPlayingState",
    0xD2D1: "NearFar",
    0xD2D2: "reserved7",
    0xD2DC: "AF_Area_Position",
    0xD2DD: "Zoom_Operation",
    0xD2E9: "ZoomAndFocusPosition_Save",
    0xD2EA: "ZoomAndFocusPosition_Load",
    0xD2EC: "ColortempStep",
    0xD2ED: "WhiteBalanceTintStep",
    0xD2EF: "Focus_Operation",
    0xF000: "ShutterECSNumberStep",
    0xD2E4: "RemoteTouchOperation",
    0xD2F2: "ZoomAndFocusPresetZoomOnly_Set",
    0xD2DF: "CustomWB_Capture_Standby",
    0xD2E0: "CustomWB_Capture_Standby_Cancel",
    0xD2E1: "CustomWB_Capture",
    0xF003: "ZoomOperationWithInt16",
    0xF004: "FocusOperationWithInt16",
    0xD2E3: "HighResolutionShutterSpeedAdjust",
    0xD2F0: "HighResolutionShutterSpeedAdjustInIntegralMultiples",
    0xE0F6: "Movie_AngleOfViewPriority",
    0xE0D6: "WindNoiseReductForExternalMic",
    0xE0D7: "NoiseCutFilter",
    0xE0D8: "NoiseCutFilterForExternalMic",
    0xE107: "DispModeCandidateStill",
    0xE108: "DispModeSettingStill",
    0xE109: "DispModeStill",
    0xE10A: "DispModeCandidateMovie",
    0xE10B: "DispModeSettingMovie",
    0xE10C: "DispModeMovie",
    0xE0DB: "CompRAWShootingHDR",
    0xE0DC: "CompRAWShootingHDRDRSetting",
    0xE0DD: "CompRAWShootingHDRFileCompressionType",
    0xE0DE: "CompRAWShootingHDRNumberOfSheets",
    0xE081: "ControlGeneralSettingFileEnableStatus",
    0xE11A: "PeakingDisplay",
    0xE11B: "PeakingLevel",
    0xE11C: "PeakingColor",
    0xE11D: "ZebraDisplay",
    0xE11E: "ZebraLevel",
    0xE11F: "ZebraLevelTypeCustom",
    0xE120: "ZebraLevelStandardCustom",
    0xE121: "ZebraLevelRangeCustom",
    0xE122: "ZebraLevelLowerLimitCustom",
    0xE123: "MarkerDisplay",
    0xE124: "CenterMarkerDisplay",
    0xE125: "AspectMarkerRatioMovie",
    0xE126: "SafetyZoneDisplay",
    0xE127: "GuideframeDisplay",
    0xE12A: "DualGain",
    0xE131: "ImagerMode",
    0xE133: "DisplayQualityForFinderOnly",
    0xE134: "DisplayQualityForMonitorOnly",
    # --- Creators' App wire-only properties (no SDK translation code) ---
    0x5004: "CompressionSetting",
    0xD059: "BaseLookImportCommandVersion",
    0xD128: "TouchExposureBiasCompensation",
    0xD12B: "WiFiDirectModeOffEnableStatus",
    0xD1A0: "AspectMarkerDisplay",
    0xD1A1: "AspectMarkerRatio",
    0xD1C0: "UploadFileCheckCommandVersion",
    0xD1D3: "LicenseUploadCommandVersion",
    0xD1D8: "SelectOnCameraTransferContentsListStatus",
    0xD1D9: "SelectOnCameraTransferResourceStatus",
    0xD206: "LicenseUploadStatus",
    0xD212: "Saturation",
    0xD217: "AELockIndication",
    0xD21A: "DisableIndication",
    0xD21F: "FELockIndication",
    0xD224: "ExposureCompensation",
    0xD226: "ISOSensitivityAbsoluteValue",
    0xD227: "MediaFormatState",
    0xD228: "OperatingMode",
    0xD22B: "ExternalSynchronizationState",
    0xD22D: "FocusMagnifierStatus",
    0xD22E: "FocusMagnifierRatio",
    0xD22F: "CurrentFocusMagnifierRatio",
    0xD230: "FocusMagnifierPosition",
    0xD232: "AFAreaPosition",
    0xD233: "FocusMagnifierButtonEnableStatus",
    0xD235: "NearFarEnableStatus",
    0xD236: "AFMFHoldButtonEnableStatus",
    0xD238: "CancelPixelShiftShootingButtonEnableStatus",
    0xD23E: "NEARModeInPF",
    0xD240: "CreativeStyle",
    0xD243: "HFRRecordingSetting",
    0xD244: "HFRFrameRate",
    0xD245: "HFRPrioritySetting",
    0xD246: "HFRRECTiming",
    0xD247: "ShootModeForMR",
    0xD24B: "TCSyncState",
    0xD24C: "FocalPosition",
    0xD24D: "DateTimeSettingStatus",
    0xD24E: "AWBLockIndication",
    0xD259: "LocationInfoLink",
    0xD265: "OnePushAFExecutionState",
    0xD266: "OnePushAFOperationEnableStatus",
    0xD278: "LiveViewUrl",
    0xD295: "ContentsTransferEnableStatus",
    0xD296: "WiFiPowerOffEnableStatus",
    0xD2A3: "StepZoomMagnificationSetting",
    0xD2B9: "ShortVideoLengthSetting",
    0xE0F7: "SharedSettingDataOperationCommandVersion",
    0xE116: "GetContentDataCommandVersion",
    0xE12F: "MyStyleFileCommandVersion",
    0xE130: "MyStyleNumber",
}


PROPERTY_INFO = {
    0x0100: (0x5007, 2, 0, 2, 0),  # FNumber
    0x0101: (0x5010, 2, 0, 2, 0),  # ExposureBiasCompensation
    0x0102: (0xD200, 2, 0, 2, 0),  # FlashCompensation
    0x0103: (0xD20D, 2, 0, 2, 0),  # ShutterSpeed
    0x0104: (0xD21E, 2, 0, 2, 0),  # IsoSensitivity
    0x0105: (0x500E, 3, 0, 3, 0),  # ExposureProgramMode
    0x0106: (0xD253, 3, 0, 3, 0),  # FileType
    0x012B: (0xD28B, 3, 0, 3, 0),  # MediaSLOT1_FileType
    0x012C: (0xD28C, 3, 0, 3, 0),  # MediaSLOT2_FileType
    0x0107: (0xD252, 3, 0, 3, 0),  # StillImageQuality
    0x012D: (0xD28D, 3, 0, 3, 0),  # MediaSLOT1_ImageQuality
    0x012E: (0xD28E, 3, 0, 3, 0),  # MediaSLOT2_ImageQuality
    0x0108: (0x5005, 3, 0, 3, 0),  # WhiteBalance
    0x0109: (0x500A, 3, 0, 3, 0),  # FocusMode
    0x010A: (0x500B, 3, 0, 3, 0),  # MeteringMode
    0x010B: (0x500C, 3, 0, 3, 0),  # FlashMode
    0x010C: (0xD262, 3, 0, 3, 0),  # WirelessFlash
    0x010D: (0xD263, 3, 0, 3, 0),  # RedEyeReduction
    0x010E: (0x5013, 3, 0, 3, 0),  # DriveMode
    0x010F: (0xD201, 3, 0, 3, 0),  # DRO
    0x0110: (0xD203, 3, 0, 3, 0),  # ImageSize
    0x012F: (0xD28F, 3, 0, 3, 0),  # MediaSLOT1_ImageSize
    0x0130: (0xD290, 3, 0, 3, 0),  # MediaSLOT2_ImageSize
    0x0111: (0xD211, 3, 0, 3, 0),  # AspectRatio
    0x0112: (0xD21B, 3, 0, 3, 0),  # PictureEffect
    0x0113: (0xD22C, 3, 0, 3, 0),  # FocusArea
    0x0114: (0xD219, 3, 0, 3, 0),  # reserved4
    0x0115: (0xD20F, 3, 0, 3, 0),  # Colortemp
    0x0116: (0xD21C, 3, 0, 3, 0),  # ColorTuningAB
    0x0117: (0xD210, 3, 0, 3, 0),  # ColorTuningGM
    0x0118: (0xD231, 3, 0, 3, 0),  # LiveViewDisplayEffect
    0x0119: (0xD222, 3, 0, 3, 0),  # StillImageStoreDestination
    0x011A: (0xD25A, 3, 0, 3, 0),  # PriorityKeySettings
    0x011B: (0xD255, 1, 0, 5, 0),  # AFTrackingSensitivity
    0x011D: (0xD254, 3, 0, 3, 0),  # Focus_Magnifier_Setting
    0x011E: (0xD223, 3, 0, 3, 0),  # DateTime_Settings
    0x0124: (0xD25C, 0, 0, 0, 0),  # Zoom_Scale
    0x0125: (0xD25F, 1, 0, 4, 0),  # Zoom_Setting
    0x0127: (0xD241, 3, 0, 3, 0),  # Movie_File_Format
    0x0128: (0xD242, 1, 0, 69, 0),  # Movie_Recording_Setting
    0x0129: (0xD286, 3, 0, 3, 0),  # Movie_Recording_FrameRateSetting
    0x012A: (0xD287, 1, 0, 3, 0),  # CompressionFileFormatStill
    0x0131: (0xD288, 3, 0, 3, 0),  # RAW_FileCompressionType
    0x0132: (0xD289, 3, 0, 3, 0),  # MediaSLOT1_RAW_FileCompressionType
    0x0133: (0xD28A, 3, 0, 3, 0),  # MediaSLOT2_RAW_FileCompressionType
    0x0136: (0xD001, 1, 0, 2, 0),  # IrisModeSetting
    0x0137: (0xD013, 1, 0, 2, 0),  # ShutterModeSetting
    0x0138: (0xD01C, 1, 0, 2, 0),  # GainControlSetting
    0x0139: (0xD020, 1, 0, 2, 0),  # GainBaseIsoSensitivity
    0x013A: (0xD021, 1, 0, 2, 0),  # GainBaseSensitivity
    0x013B: (0xD022, 3, 0, 3, 0),  # ExposureIndex
    0x013C: (0xD03C, 3, 0, 3, 0),  # BaseLookValue
    0x013D: (0xD042, 1, 0, 2, 0),  # PlaybackMedia
    0x013E: (0xD045, 0, 0, 0, 0),  # DispModeSetting
    0x013F: (0xD046, 1, 0, 7, 0),  # DispMode
    0x0140: (0xD047, 1, 0, 3, 0),  # TouchOperation
    0x0141: (0xD048, 1, 0, 4, 0),  # SelectFinderMonitor
    0x0142: (0xD049, 1, 0, 2, 0),  # AutoPowerOffTemperature
    0x0143: (0xD04A, 1, 0, 2, 0),  # BodyKeyLock
    0x0144: (0xD092, 1, 0, 2, 0),  # ImageID_Num_Setting
    0x0145: (0xD04B, 0, 0, 0, 0),  # ImageID_Num
    0x0146: (0xD04C, 1, 0, 1, 0),  # ImageID_String
    0x0147: (0xD099, 1, 0, 2, 0),  # ExposureCtrlType
    0x0148: (0xD04D, 1, 0, 2, 0),  # MonitorLUTSetting
    0x0149: (0xD004, 0, 0, 0, 0),  # FocalDistanceInMeter
    0x014A: (0xD005, 0, 0, 0, 0),  # FocalDistanceInFeet
    0x014B: (0xD006, 1, 0, 2, 0),  # FocalDistanceUnitSetting
    0x014C: (0xD00A, 0, 0, 0, 0),  # DigitalZoomScale
    0x014D: (0xD00B, 0, 0, 0, 0),  # ZoomDistance
    0x014E: (0xD029, 1, 0, 2, 0),  # ZoomDistanceUnitSetting
    0x014F: (0xD011, 1, 0, 5, 0),  # ShutterModeStatus
    0x0150: (0xD014, 1, 0, 2, 0),  # ShutterSlow
    0x0151: (0xD015, 3, 0, 3, 0),  # ShutterSlowFrames
    0x0152: (0xD024, 2, 0, 2, 0),  # Movie_Recording_ResolutionForMain
    0x0153: (0xD025, 2, 0, 2, 0),  # Movie_Recording_ResolutionForProxy
    0x0154: (0xD028, 3, 0, 3, 0),  # Movie_Recording_FrameRateProxySetting
    0x0155: (0xD037, 1, 0, 3, 0),  # BatteryRemainDisplayUnit
    0x0156: (0xD03A, 1, 0, 3, 0),  # PowerSource
    0x0157: (0xE000, 3, 0, 3, 0),  # MovieShootingMode
    0x0158: (0xE001, 1, 0, 2, 0),  # MovieShootingModeColorGamut
    0x0159: (0xE002, 1, 0, 2, 0),  # MovieShootingModeTargetDisplay
    0x015A: (0xE009, 1, 0, 2, 0),  # DepthOfFieldAdjustmentMode
    0x015C: (0xD00C, 1, 0, 2, 0),  # WhiteBalanceModeSetting
    0x015D: (0xD00D, 0, 0, 0, 0),  # WhiteBalanceTint
    0x0160: (0xE006, 1, 0, 2, 0),  # ShutterECSSetting
    0x0161: (0xE007, 0, 0, 0, 0),  # ShutterECSNumber
    0x0163: (0xE008, 0, 0, 0, 0),  # ShutterECSFrequency
    0x0164: (0xE00D, 0, 0, 1, 0),  # RecorderControlProxySetting
    0x0165: (0xE014, 2, 0, 2, 0),  # ButtonAssignmentAssignable1
    0x0166: (0xE015, 2, 0, 2, 0),  # ButtonAssignmentAssignable2
    0x0167: (0xE016, 2, 0, 2, 0),  # ButtonAssignmentAssignable3
    0x0168: (0xE017, 2, 0, 2, 0),  # ButtonAssignmentAssignable4
    0x0169: (0xE018, 2, 0, 2, 0),  # ButtonAssignmentAssignable5
    0x016A: (0xE019, 2, 0, 2, 0),  # ButtonAssignmentAssignable6
    0x016B: (0xE01A, 2, 0, 2, 0),  # ButtonAssignmentAssignable7
    0x016C: (0xE01B, 2, 0, 2, 0),  # ButtonAssignmentAssignable8
    0x016D: (0xE01C, 2, 0, 2, 0),  # ButtonAssignmentAssignable9
    0x021F: (0xE01D, 2, 0, 2, 0),  # ButtonAssignmentAssignable10
    0x0220: (0xE08D, 2, 0, 2, 0),  # ButtonAssignmentAssignable11
    0x016E: (0xE01E, 2, 0, 2, 0),  # ButtonAssignmentLensAssignable1
    0x016F: (0xE029, 1, 0, 2, 0),  # AssignableButton1
    0x0170: (0xE02A, 1, 0, 2, 0),  # AssignableButton2
    0x0171: (0xE02B, 1, 0, 2, 0),  # AssignableButton3
    0x0172: (0xE02C, 1, 0, 2, 0),  # AssignableButton4
    0x0173: (0xE02D, 1, 0, 2, 0),  # AssignableButton5
    0x0174: (0xE02E, 1, 0, 2, 0),  # AssignableButton6
    0x0175: (0xE02F, 1, 0, 2, 0),  # AssignableButton7
    0x0176: (0xE030, 1, 0, 2, 0),  # AssignableButton8
    0x0177: (0xE031, 1, 0, 2, 0),  # AssignableButton9
    0x0225: (0xE032, 1, 0, 2, 0),  # AssignableButton10
    0x0226: (0xE08E, 1, 0, 2, 0),  # AssignableButton11
    0x0178: (0xE033, 1, 0, 2, 0),  # LensAssignableButton1
    0x0179: (0xD007, 1, 0, 2, 0),  # FocusModeSetting
    0x017A: (0xD00E, 3, 0, 3, 0),  # ShutterAngle
    0x017B: (0xD00F, 1, 0, 2, 0),  # ShutterSetting
    0x017C: (0xD010, 1, 0, 2, 0),  # ShutterMode
    0x017D: (0xD016, 2, 0, 2, 0),  # ShutterSpeedValue
    0x017E: (0xD018, 1, 0, 2, 0),  # NDFilter
    0x017F: (0xD01A, 1, 0, 2, 0),  # NDFilterModeSetting
    0x0180: (0xD01B, 2, 0, 2, 0),  # NDFilterValue
    0x0181: (0xD01D, 1, 0, 2, 0),  # GainUnitSetting
    0x0182: (0xD01E, 0, 0, 0, 0),  # GaindBValue
    0x0183: (0xD03B, 1, 0, 2, 0),  # AWB
    0x0184: (0xE01F, 2, 0, 2, 0),  # SceneFileIndex
    0x0185: (0xE021, 1, 0, 2, 0),  # MoviePlayButton
    0x0186: (0xE022, 1, 0, 2, 0),  # MoviePlayPauseButton
    0x0187: (0xE023, 1, 0, 2, 0),  # MoviePlayStopButton
    0x0188: (0xE024, 1, 0, 2, 0),  # MovieForwardButton
    0x0189: (0xE025, 1, 0, 2, 0),  # MovieRewindButton
    0x018A: (0xE026, 1, 0, 2, 0),  # MovieNextButton
    0x018B: (0xE027, 1, 0, 2, 0),  # MoviePrevButton
    0x018C: (0xE028, 1, 0, 2, 0),  # MovieRecReviewButton
    0x018D: (0xD060, 1, 0, 3, 0),  # SubjectRecognitionAF
    0x018E: (0xD061, 0, 0, 0, 0),  # AFTransitionSpeed
    0x018F: (0xD062, 0, 0, 0, 0),  # AFSubjShiftSens
    0x0190: (0xE084, 1, 0, 2, 0),  # AFAssist
    0x0191: (0xD073, 1, 0, 3, 0),  # NDFilterSwitchingSetting
    0x0192: (0xE083, 1, 0, 3, 0),  # FunctionOfRemoteTouchOperation
    0x0194: (0xE088, 0, 0, 0, 0),  # FollowFocusPositionSetting
    0x0195: (0xD2A1, 0, 0, 0, 0),  # FocusBracketShotNumber
    0x0196: (0xD2A2, 0, 0, 0, 0),  # FocusBracketFocusRange
    0x0197: (0xD0C5, 1, 0, 2, 0),  # ExtendedInterfaceMode
    0x0198: (0xD0D0, 3, 0, 3, 0),  # SQRecordingFrameRateSetting
    0x0199: (0xD052, 3, 0, 3, 0),  # SQFrameRate
    0x019A: (0xD0D1, 3, 0, 3, 0),  # SQRecordingSetting
    0x019B: (0xD0D2, 0, 0, 1, 0),  # AudioRecording
    0x019C: (0xE050, 0, 0, 0, 0),  # AudioInputMasterLevel
    0x019D: (0xD0D3, 0, 0, 0, 0),  # TimeCodePreset
    0x019E: (0xD0D5, 1, 0, 2, 0),  # TimeCodeFormat
    0x019F: (0xD0D6, 1, 0, 2, 0),  # TimeCodeRun
    0x01A0: (0xD0D7, 1, 0, 2, 0),  # TimeCodeMake
    0x01A1: (0xD0D4, 0, 0, 0, 0),  # UserBitPreset
    0x01A2: (0xD0D8, 1, 0, 2, 0),  # UserBitTimeRec
    0x01A3: (0xD0D9, 1, 0, 2, 0),  # ImageStabilizationSteadyShot
    0x01A4: (0xD0DA, 1, 0, 4, 0),  # Movie_ImageStabilizationSteadyShot
    0x01A5: (0xD0DB, 1, 0, 2, 0),  # SilentMode
    0x01A6: (0xD0DC, 1, 0, 3, 0),  # SilentModeApertureDriveInAF
    0x01A7: (0xD0DD, 1, 0, 2, 0),  # SilentModeShutterWhenPowerOff
    0x01A8: (0xD0DE, 1, 0, 2, 0),  # SilentModeAutoPixelMapping
    0x01A9: (0xD0DF, 1, 0, 3, 0),  # ShutterType
    0x01AA: (0xD23F, 3, 0, 3, 0),  # PictureProfile
    0x01AB: (0xD0E0, 0, 0, 0, 0),  # PictureProfile_BlackLevel
    0x01AC: (0xD0E1, 3, 0, 3, 0),  # PictureProfile_Gamma
    0x01AD: (0xD0E2, 1, 0, 3, 0),  # PictureProfile_BlackGammaRange
    0x01AE: (0xD0E3, 0, 0, 0, 0),  # PictureProfile_BlackGammaLevel
    0x01AF: (0xD0E4, 1, 0, 2, 0),  # PictureProfile_KneeMode
    0x01B0: (0xD0E5, 3, 0, 3, 0),  # PictureProfile_KneeAutoSet_MaxPoint
    0x01B1: (0xD0E6, 1, 0, 3, 0),  # PictureProfile_KneeAutoSet_Sensitivity
    0x01B2: (0xD0E7, 3, 0, 3, 0),  # PictureProfile_KneeManualSet_Point
    0x01B3: (0xD0E8, 0, 0, 0, 0),  # PictureProfile_KneeManualSet_Slope
    0x01B4: (0xD0E9, 1, 0, 13, 0),  # PictureProfile_ColorMode
    0x01B5: (0xD0EA, 0, 0, 0, 0),  # PictureProfile_Saturation
    0x01B6: (0xD0EB, 0, 0, 0, 0),  # PictureProfile_ColorPhase
    0x01B7: (0xD0EC, 0, 0, 0, 0),  # PictureProfile_ColorDepthRed
    0x01B8: (0xD0ED, 0, 0, 0, 0),  # PictureProfile_ColorDepthGreen
    0x01B9: (0xD0EE, 0, 0, 0, 0),  # PictureProfile_ColorDepthBlue
    0x01BA: (0xD0EF, 0, 0, 0, 0),  # PictureProfile_ColorDepthCyan
    0x01BB: (0xD0F0, 0, 0, 0, 0),  # PictureProfile_ColorDepthMagenta
    0x01BC: (0xD0F1, 0, 0, 0, 0),  # PictureProfile_ColorDepthYellow
    0x01BD: (0xD0F2, 0, 0, 0, 0),  # PictureProfile_DetailLevel
    0x01BE: (0xD0F3, 1, 0, 2, 0),  # PictureProfile_DetailAdjustMode
    0x01BF: (0xD0F4, 0, 0, 0, 0),  # PictureProfile_DetailAdjustVHBalance
    0x01C0: (0xD0F5, 3, 0, 3, 0),  # PictureProfile_DetailAdjustBWBalance
    0x01C1: (0xD0F6, 0, 0, 0, 0),  # PictureProfile_DetailAdjustLimit
    0x01C2: (0xD0F7, 0, 0, 0, 0),  # PictureProfile_DetailAdjustCrispening
    0x01C3: (0xD0F8, 0, 0, 0, 0),  # PictureProfile_DetailAdjustHiLightDetail
    0x01C4: (0xD0F9, 3, 0, 3, 0),  # PictureProfile_Copy
    0x01C5: (0xD0FA, 3, 0, 3, 0),  # CreativeLook
    0x01C6: (0xD0FB, 0, 0, 0, 0),  # CreativeLook_Contrast
    0x01C7: (0xD0FC, 0, 0, 0, 0),  # CreativeLook_Highlights
    0x01C8: (0xD0FD, 0, 0, 0, 0),  # CreativeLook_Shadows
    0x01C9: (0xD0FE, 0, 0, 0, 0),  # CreativeLook_Fade
    0x01CA: (0xD0FF, 0, 0, 0, 0),  # CreativeLook_Saturation
    0x01CB: (0xD100, 0, 0, 0, 0),  # CreativeLook_Sharpness
    0x01CC: (0xD101, 0, 0, 0, 0),  # CreativeLook_SharpnessRange
    0x01CD: (0xD102, 0, 0, 0, 0),  # CreativeLook_Clarity
    0x01CE: (0xD103, 2, 0, 2, 0),  # CreativeLook_CustomLook
    0x01CF: (0xD027, 3, 0, 3, 0),  # Movie_ProxyFileFormat
    0x01D0: (0xD109, 1, 0, 3, 0),  # ProxyRecordingSetting
    0x01D1: (0xD283, 1, 0, 11, 0),  # FunctionOfTouchOperation
    0x01D2: (0xD281, 0, 0, 1, 0),  # HighResolutionShutterSpeedSetting
    0x01D3: (0xD0C7, 3, 0, 3, 0),  # DeleteUserBaseLook
    0x01D4: (0xD0C8, 3, 0, 3, 0),  # SelectUserBaseLookToEdit
    0x01D5: (0xD0CC, 3, 0, 3, 0),  # SelectUserBaseLookToSetInPPLUT
    0x01D6: (0xD0C9, 1, 0, 2, 0),  # UserBaseLookInput
    0x01D7: (0xD0CA, 2, 0, 2, 0),  # UserBaseLookAELevelOffset
    0x01D8: (0xD0CB, 2, 0, 2, 0),  # BaseISOSwitchEI
    0x01D9: (0xD133, 1, 0, 2, 0),  # FlickerLessShooting
    0x01DA: (0xD172, 1, 0, 2, 0),  # AudioLevelDisplay
    0x01DB: (0xD17C, 0, 0, 0, 0),  # PlaybackVolumeSettings
    0x01DC: (0xD17D, 2, 0, 2, 0),  # AutoReview
    0x01DD: (0xD17E, 1, 0, 4, 0),  # AudioSignals
    0x01DE: (0xD17F, 3, 0, 3, 0),  # HDMIResolutionStillPlay
    0x01DF: (0xD180, 1, 0, 2, 0),  # Movie_HDMIOutputRecMedia
    0x01E0: (0xD181, 3, 0, 3, 0),  # Movie_HDMIOutputResolution
    0x01E1: (0xD182, 3, 0, 3, 0),  # Movie_HDMIOutput4KSetting
    0x01E2: (0xD183, 1, 0, 2, 0),  # Movie_HDMIOutputRAW
    0x01E3: (0xD184, 1, 0, 6, 0),  # Movie_HDMIOutputRawSetting
    0x01E4: (0xD185, 1, 0, 2, 0),  # Movie_HDMIOutputColorGamutForRAWOut
    0x01E5: (0xD186, 1, 0, 2, 0),  # Movie_HDMIOutputTimeCode
    0x01E6: (0xD187, 1, 0, 2, 0),  # Movie_HDMIOutputRecControl
    0x01E8: (0xD079, 1, 0, 2, 0),  # MonitoringOutputDisplayHDMI
    0x01E9: (0xE059, 3, 0, 3, 0),  # Movie_HDMIOutputAudioCH
    0x01EA: (0xD055, 3, 0, 3, 0),  # Movie_IntervalRec_IntervalTime
    0x01EB: (0xD151, 3, 0, 3, 0),  # Movie_IntervalRec_FrameRateSetting
    0x01EC: (0xD152, 38, 0, 69, 0),  # Movie_IntervalRec_RecordingSetting
    0x01ED: (0xD0CD, 1, 0, 3, 0),  # EframingScaleAuto
    0x01EE: (0xD0CE, 0, 0, 0, 0),  # EframingSpeedAuto
    0x01EF: (0xD124, 1, 0, 4, 0),  # EframingModeAuto
    0x01F0: (0xD153, 1, 0, 2, 0),  # EframingRecordingImageCrop
    0x01F1: (0xD154, 1, 0, 2, 0),  # EframingHDMICrop
    0x01F2: (0xD0CF, 1, 0, 2, 0),  # CameraEframing
    0x01F3: (0xD150, 1, 0, 5, 0),  # USBPowerSupply
    0x01F4: (0xD15B, 1, 0, 2, 0),  # LongExposureNR
    0x01F5: (0xD15C, 1, 0, 4, 0),  # HighIsoNR
    0x01F6: (0xD15D, 1, 0, 2, 0),  # HLGStillImage
    0x01F7: (0xD15E, 1, 0, 2, 0),  # ColorSpace
    0x01F8: (0xD166, 1, 0, 2, 0),  # BracketOrder
    0x01F9: (0xD167, 1, 0, 2, 0),  # FocusBracketOrder
    0x01FA: (0xD168, 1, 0, 2, 0),  # FocusBracketExposureLock1stImg
    0x01FB: (0xD169, 3, 0, 3, 0),  # FocusBracketIntervalUntilNextShot
    0x01FC: (0xD16A, 0, 0, 0, 0),  # IntervalRec_ShootingStartTime
    0x01FD: (0xD16B, 0, 0, 0, 0),  # IntervalRec_ShootingInterval
    0x01FE: (0xD16F, 1, 0, 2, 0),  # IntervalRec_ShootIntervalPriority
    0x01FF: (0xD16C, 0, 0, 0, 0),  # IntervalRec_NumberOfShots
    0x0200: (0xD16D, 1, 0, 4, 0),  # IntervalRec_AETrackingSensitivity
    0x0201: (0xD16E, 1, 0, 3, 0),  # IntervalRec_ShutterType
    0x0202: (0xD170, 1, 0, 2, 0),  # ElectricFrontCurtainShutter
    0x0203: (0xD171, 1, 0, 3, 0),  # WindNoiseReduct
    0x0204: (0xD29C, 0, 0, 1, 0),  # RecordingSelfTimer
    0x0205: (0xD29D, 2, 0, 2, 0),  # RecordingSelfTimerCountTime
    0x0206: (0xD29F, 0, 0, 1, 0),  # RecordingSelfTimerContinuous
    0x0207: (0xD2A0, 4, 0, 4, 0),  # RecordingSelfTimerStatus
    0x0208: (0xD2A4, 0, 0, 1, 0),  # BulbTimerSetting
    0x0209: (0xD2A5, 0, 0, 0, 0),  # BulbExposureTimeSetting
    0x020A: (0xD173, 1, 0, 2, 0),  # AutoSlowShutter
    0x020B: (0xD14D, 1, 0, 2, 0),  # IsoAutoMinShutterSpeedMode
    0x020C: (0xD176, 2, 0, 2, 0),  # IsoAutoMinShutterSpeedManual
    0x020D: (0xD177, 1, 0, 5, 0),  # IsoAutoMinShutterSpeedPreset
    0x020E: (0xE042, 0, 0, 0, 0),  # FocusPositionSetting
    0x020F: (0xD178, 1, 0, 4, 0),  # SoftSkinEffect
    0x0210: (0xD179, 1, 0, 3, 0),  # PrioritySetInAF_S
    0x0211: (0xD17A, 1, 0, 3, 0),  # PrioritySetInAF_C
    0x0212: (0xD17B, 2, 0, 2, 0),  # FocusMagnificationTime
    0x0213: (0xD157, 1, 0, 2, 0),  # SubjectRecognitionInAF
    0x0214: (0xD158, 3, 0, 3, 0),  # RecognitionTarget
    0x0215: (0xD159, 1, 0, 3, 0),  # RightLeftEyeSelect
    0x0216: (0xD27C, 2, 0, 2, 0),  # SelectFTPServer
    0x0217: (0xD02E, 2, 0, 2, 0),  # SelectFTPServerID
    0x0218: (0xD041, 1, 0, 2, 0),  # FTP_Function
    0x0219: (0xD04E, 1, 0, 2, 0),  # FTP_AutoTransfer
    0x021A: (0xD04F, 1, 0, 3, 0),  # FTP_AutoTransferTarget
    0x021B: (0xD199, 1, 0, 3, 0),  # Movie_FTP_AutoTransferTarget
    0x021C: (0xD19A, 1, 0, 3, 0),  # FTP_TransferTarget
    0x021D: (0xD14B, 1, 0, 3, 0),  # Movie_FTP_TransferTarget
    0x021E: (0xD14C, 1, 0, 2, 0),  # FTP_PowerSave
    0x022B: (0xD14E, 1, 0, 2, 0),  # NDFilterUnitSetting
    0x022C: (0xD14F, 3, 0, 3, 0),  # NDFilterOpticalDensityValue
    0x022D: (0xD000, 3, 0, 3, 0),  # TNumber
    0x022E: (0xD003, 1, 0, 3, 0),  # IrisDisplayUnit
    0x022F: (0xE080, 1, 0, 3, 0),  # Movie_ImageStabilizationLevel
    0x0230: (0xD192, 1, 0, 2, 0),  # ImageStabilizationSteadyShotAdjust
    0x0231: (0xD193, 2, 0, 2, 0),  # ImageStabilizationSteadyShotFocalLength
    0x0232: (0xD19F, 2, 0, 2, 0),  # ExtendedShutterSpeed
    0x0233: (0xD208, 3, 0, 3, 0),  # CameraButtonFunction
    0x0234: (0xD209, 3, 0, 3, 0),  # CameraButtonFunctionMulti
    0x0235: (0xD20A, 3, 0, 3, 0),  # CameraDialFunction
    0x0236: (0xD155, 1, 0, 2, 0),  # SynchroterminalForcedOutput
    0x0237: (0xD156, 1, 0, 3, 0),  # ShutterReleaseTimeLagControl
    0x0238: (0xD12F, 2, 0, 2, 0),  # ContinuousShootingSpotBoostFrameSpeed
    0x0239: (0xD189, 1, 0, 2, 0),  # TimeShiftShooting
    0x023A: (0xD18A, 1, 0, 3, 0),  # TimeShiftTriggerSetting
    0x023B: (0xD18B, 2, 0, 2, 0),  # TimeShiftPreShootingTimeSetting
    0x023C: (0xD196, 1, 0, 2, 0),  # EmbedLUTFile
    0x023D: (0xD1C7, 1, 0, 3, 0),  # APS_C_S35
    0x023E: (0xD1A2, 1, 0, 3, 0),  # LensCompensationShading
    0x023F: (0xD1A3, 1, 0, 2, 0),  # LensCompensationChromaticAberration
    0x0240: (0xD1A4, 1, 0, 2, 0),  # LensCompensationDistortion
    0x0241: (0xD1A5, 1, 0, 2, 0),  # LensCompensationBreathing
    0x0242: (0xD15F, 3, 0, 3, 0),  # RecordingMedia
    0x0243: (0xD160, 3, 0, 3, 0),  # Movie_RecordingMedia
    0x0244: (0xD161, 1, 0, 2, 0),  # AutoSwitchMedia
    0x0245: (0xD1C8, 1, 0, 2, 0),  # RecordingFileNumber
    0x0246: (0xD2B5, 1, 0, 2, 0),  # Movie_RecordingFileNumber
    0x0247: (0xD1CA, 1, 0, 1, 0),  # RecordingSettingFileName
    0x0248: (0xD1CB, 1, 0, 2, 0),  # RecordingFolderFormat
    0x024A: (0xD132, 2, 0, 2, 0),  # SelectIPTCMetadata
    0x024B: (0xD1CD, 1, 0, 2, 0),  # WriteCopyrightInfo
    0x024C: (0xD1CE, 1, 0, 1, 0),  # SetPhotographer
    0x024D: (0xD1CF, 1, 0, 1, 0),  # SetCopyright
    0x024E: (0xD1DC, 1, 0, 1, 0),  # FileSettingsTitleNameSettings
    0x024F: (0xD1A6, 1, 0, 2, 0),  # FocusBracketRecordingFolder
    0x0250: (0xD1A7, 1, 0, 2, 0),  # ReleaseWithoutLens
    0x0251: (0xD1A8, 1, 0, 2, 0),  # ReleaseWithoutCard
    0x0252: (0xD1DE, 1, 0, 2, 0),  # GridLineDisplay
    0x0253: (0xD162, 3, 0, 3, 0),  # ContinuousShootingSpeedInElectricShutterHiPlus
    0x0254: (0xD163, 3, 0, 3, 0),  # ContinuousShootingSpeedInElectricShutterHi
    0x0255: (0xD164, 3, 0, 3, 0),  # ContinuousShootingSpeedInElectricShutterMid
    0x0256: (0xD165, 3, 0, 3, 0),  # ContinuousShootingSpeedInElectricShutterLo
    0x0257: (0xD1B6, 2, 0, 2, 0),  # IsoAutoRangeLimitMin
    0x0258: (0xD1B7, 2, 0, 2, 0),  # IsoAutoRangeLimitMax
    0x0259: (0xD1E5, 1, 0, 2, 0),  # FacePriorityInMultiMetering
    0x025A: (0xD1AA, 1, 0, 3, 0),  # PrioritySetInAWB
    0x025B: (0xD135, 1, 0, 3, 0),  # CustomWB_Size_Setting
    0x025C: (0xD1AB, 1, 0, 2, 0),  # AFIlluminator
    0x025D: (0xD1AC, 1, 0, 3, 0),  # ApertureDriveInAF
    0x025E: (0xD1AD, 1, 0, 2, 0),  # AFWithShutter
    0x025F: (0xD1AE, 1, 0, 2, 0),  # FullTimeDMF
    0x0260: (0xD1AF, 1, 0, 2, 0),  # PreAF
    0x0261: (0xD1E6, 0, 0, 0, 0),  # SubjectRecognitionPersonTrackingSubjectShiftRange
    0x0262: (0xD1E7, 1, 0, 3, 0),  # SubjectRecognitionAnimalBirdPriority
    0x0263: (0xD1E8, 3, 0, 3, 0),  # SubjectRecognitionAnimalBirdDetectionParts
    0x0264: (0xD1E9, 0, 0, 0, 0),  # SubjectRecognitionAnimalTrackingSubjectShiftRange
    0x0265: (0xD1EA, 0, 0, 0, 0),  # SubjectRecognitionAnimalTrackingSensitivity
    0x0266: (0xD1EB, 0, 0, 0, 0),  # SubjectRecognitionAnimalDetectionSensitivity
    0x0267: (0xD1EC, 1, 0, 3, 0),  # SubjectRecognitionAnimalDetectionParts
    0x0268: (0xD1ED, 0, 0, 0, 0),  # SubjectRecognitionBirdTrackingSubjectShiftRange
    0x0269: (0xD1EE, 0, 0, 0, 0),  # SubjectRecognitionBirdTrackingSensitivity
    0x026A: (0xD1EF, 0, 0, 0, 0),  # SubjectRecognitionBirdDetectionSensitivity
    0x026B: (0xD1F0, 1, 0, 3, 0),  # SubjectRecognitionBirdDetectionParts
    0x026C: (0xD1F1, 0, 0, 0, 0),  # SubjectRecognitionInsectTrackingSubjectShiftRange
    0x026D: (0xD1F2, 0, 0, 0, 0),  # SubjectRecognitionInsectTrackingSensitivity
    0x026E: (0xD1F3, 0, 0, 0, 0),  # SubjectRecognitionInsectDetectionSensitivity
    0x026F: (0xD1F4, 0, 0, 0, 0),  # SubjectRecognitionCarTrainTrackingSubjectShiftRange
    0x0270: (0xD1F5, 0, 0, 0, 0),  # SubjectRecognitionCarTrainTrackingSensitivity
    0x0271: (0xD1F6, 0, 0, 0, 0),  # SubjectRecognitionCarTrainDetectionSensitivity
    0x0272: (0xD1F7, 0, 0, 0, 0),  # SubjectRecognitionPlaneTrackingSubjectShiftRange
    0x0273: (0xD1F8, 0, 0, 0, 0),  # SubjectRecognitionPlaneTrackingSensitivity
    0x0274: (0xD1F9, 0, 0, 0, 0),  # SubjectRecognitionPlaneDetectionSensitivity
    0x0275: (0xD1FA, 1, 0, 2, 0),  # SubjectRecognitionPriorityOnRegisteredFace
    0x0276: (0xD1B8, 1, 0, 2, 0),  # FaceEyeFrameDisplay
    0x0277: (0xD1B9, 1, 0, 2, 0),  # FocusMap
    0x0278: (0xD1BD, 2, 0, 2, 0),  # InitialFocusMagnifier
    0x0279: (0xD1BA, 1, 0, 2, 0),  # AFInFocusMagnifier
    0x027A: (0xD2AD, 1, 0, 3, 0),  # AFTrackForSpeedChange
    0x027B: (0xD138, 3, 0, 3, 0),  # AFFreeSizeAndPositionSetting
    0x027D: (0xD2B2, 1, 0, 2, 0),  # PlaySetOfMultiMedia
    0x027E: (0xD1BE, 1, 0, 2, 0),  # RemoteSaveImageSize
    0x027F: (0xD14A, 1, 0, 2, 0),  # FTP_TransferStillImageQualitySize
    0x0280: (0xD216, 1, 0, 2, 0),  # FTP_AutoTransferTarget_StillImage
    0x0281: (0xD225, 1, 0, 2, 0),  # ProtectImageInFTPTransfer
    0x0282: (0xD1FB, 1, 0, 2, 0),  # MonitorBrightnessType
    0x0283: (0xD1FC, 0, 0, 0, 0),  # MonitorBrightnessManual
    0x0284: (0xD1B0, 1, 0, 2, 0),  # DisplayQualityFinderMonitor
    0x0285: (0xD1FD, 1, 0, 4, 0),  # TCUBDisplaySetting
    0x0286: (0xD1FE, 1, 0, 2, 0),  # GammaDisplayAssist
    0x0287: (0xD1FF, 1, 0, 1026, 0),  # GammaDisplayAssistType
    0x0288: (0xD220, 1, 0, 2, 0),  # AudioSignalsStartEnd
    0x0289: (0xD1B1, 0, 0, 0, 0),  # AudioSignalsVolume
    0x028A: (0xD1B2, 1, 0, 2, 0),  # ControlForHDMI
    0x028B: (0xD1B3, 1, 0, 2, 0),  # AntidustShutterWhenPowerOff
    0x028C: (0xD1C1, 1, 0, 2, 0),  # WakeOnLAN
    0x0501: (0xD239, 3, 0, 3, 0),  # reserved10
    0x0502: (0xD23A, 3, 0, 3, 0),  # reserved11
    0x0503: (0xD23B, 3, 0, 3, 0),  # reserved12
    0x0505: (0xD24F, 3, 0, 3, 0),  # Interval_Rec_Mode
    0x0506: (0xD268, 3, 0, 3, 0),  # Still_Image_Trans_Size
    0x0507: (0xD269, 3, 0, 3, 0),  # RAW_J_PC_Save_Image
    0x0508: (0xD26A, 3, 0, 3, 0),  # LiveView_Image_Quality
    0x050C: (0xD299, 1, 0, 2, 0),  # Remocon_Zoom_Speed_Type
    0x0701: (0xD215, 4, 0, 4, 0),  # SnapshotInfo
    0x0702: (0xD218, 4, 0, 4, 0),  # BatteryRemain
    0x0703: (0xD20E, 4, 0, 4, 0),  # BatteryLevel
    0x0704: (0xD214, 4, 0, 4, 0),  # EstimatePictureSize
    0x0705: (0xD21D, 4, 0, 4, 0),  # RecordingState
    0x0706: (0xD221, 4, 0, 4, 0),  # LiveViewStatus
    0x0707: (0xD213, 4, 0, 4, 0),  # FocusIndication
    0x0708: (0xD248, 4, 0, 4, 0),  # MediaSLOT1_Status
    0x0709: (0xD249, 4, 0, 4, 0),  # MediaSLOT1_RemainingNumber
    0x070A: (0xD24A, 4, 0, 4, 0),  # MediaSLOT1_RemainingTime
    0x070B: (0xD279, 4, 0, 4, 0),  # MediaSLOT1_FormatEnableStatus
    0x070C: (0xD27D, 4, 0, 4, 0),  # reserved20
    0x070D: (0xD256, 4, 0, 4, 0),  # MediaSLOT2_Status
    0x070E: (0xD27A, 4, 0, 4, 0),  # MediaSLOT2_FormatEnableStatus
    0x070F: (0xD257, 4, 0, 4, 0),  # MediaSLOT2_RemainingNumber
    0x0710: (0xD258, 4, 0, 4, 0),  # MediaSLOT2_RemainingTime
    0x0711: (0xD27E, 4, 0, 4, 0),  # reserved22
    0x0712: (0xD27B, 4, 0, 4, 0),  # Media_FormatProgressRate
    0x0713: (0xD27F, 4, 0, 4, 0),  # FTP_ConnectionStatus
    0x0714: (0xD280, 4, 0, 4, 0),  # FTP_ConnectionErrorInfo
    0x0715: (0xD267, 4, 0, 4, 0),  # LiveView_Area
    0x0716: (0xD23C, 4, 0, 4, 0),  # reserved26
    0x0717: (0xD23D, 4, 0, 4, 0),  # reserved27
    0x0718: (0xD250, 4, 0, 4, 0),  # Interval_Rec_Status
    0x0719: (0xD270, 4, 0, 4, 0),  # CustomWB_Execution_State
    0x071A: (0xD26B, 4, 0, 4, 0),  # CustomWB_Capturable_Area
    0x071B: (0xD26C, 4, 0, 4, 0),  # CustomWB_Capture_Frame_Size
    0x071C: (0xD26F, 4, 0, 4, 0),  # CustomWB_Capture_Operation
    0x071E: (0xD25B, 4, 0, 4, 0),  # Zoom_Operation_Status
    0x071F: (0xD25D, 4, 0, 4, 0),  # Zoom_Bar_Information
    0x0720: (0xD260, 4, 0, 4, 0),  # Zoom_Type_Status
    0x0721: (0xD292, 4, 0, 4, 0),  # MediaSLOT1_QuickFormatEnableStatus
    0x0722: (0xD293, 4, 0, 4, 0),  # MediaSLOT2_QuickFormatEnableStatus
    0x0723: (0xD294, 4, 0, 4, 0),  # Cancel_Media_FormatEnableStatus
    0x0724: (0xD25E, 4, 0, 4, 0),  # Zoom_Speed_Range
    0x0729: (0xD023, 4, 0, 4, 0),  # IsoCurrentSensitivity
    0x072A: (0xD271, 4, 0, 4, 0),  # CameraSetting_SaveOperationEnableStatus
    0x072B: (0xD272, 4, 0, 4, 0),  # CameraSetting_ReadOperationEnableStatus
    0x072C: (0xD273, 4, 0, 4, 0),  # CameraSetting_SaveRead_State
    0x072D: (0xD043, 4, 0, 4, 0),  # CameraSettingsResetEnableStatus
    0x072E: (0xD29A, 4, 0, 4, 0),  # APS_C_or_Full_SwitchingSetting
    0x072F: (0xD29B, 4, 0, 4, 0),  # APS_C_or_Full_SwitchingEnableStatus
    0x0730: (0xD044, 4, 0, 4, 0),  # DispModeCandidate
    0x0731: (0xD017, 4, 0, 4, 0),  # ShutterSpeedCurrentValue
    0x0732: (0xD008, 4, 0, 4, 0),  # Focus_Speed_Range
    0x0733: (0xD019, 4, 0, 4, 0),  # NDFilterMode
    0x0734: (0xD030, 4, 0, 4, 0),  # MoviePlayingSpeed
    0x0735: (0xD035, 4, 0, 4, 0),  # MediaSLOT1Player
    0x0736: (0xD036, 4, 0, 4, 0),  # MediaSLOT2Player
    0x0737: (0xD038, 4, 0, 4, 0),  # BatteryRemainingInMinutes
    0x0738: (0xD039, 4, 0, 4, 0),  # BatteryRemainingInVoltage
    0x0739: (0xD03E, 4, 0, 4, 0),  # DCVoltage
    0x073A: (0xD02F, 4, 0, 4, 0),  # MoviePlayingState
    0x073B: (0xE004, 4, 0, 4, 0),  # FocusTouchSpotStatus
    0x073C: (0xE005, 4, 0, 4, 0),  # FocusTrackingStatus
    0x073D: (0xE00A, 4, 0, 4, 0),  # DepthOfFieldAdjustmentInterlockingMode
    0x073E: (0xE00B, 4, 0, 4, 0),  # RecorderClipName
    0x073F: (0xE00C, 4, 0, 4, 0),  # RecorderControlMainSetting
    0x0740: (0xE00E, 4, 0, 4, 0),  # RecorderStartMain
    0x0741: (0xE00F, 4, 0, 4, 0),  # RecorderStartProxy
    0x0742: (0xE010, 4, 0, 4, 0),  # RecorderMainStatus
    0x0743: (0xE011, 4, 0, 4, 0),  # RecorderProxyStatus
    0x0744: (0xE012, 4, 0, 4, 0),  # RecorderExtRawStatus
    0x0745: (0xE013, 4, 0, 4, 0),  # RecorderSaveDestination
    0x0746: (0xE035, 4, 0, 4, 0),  # AssignableButtonIndicator1
    0x0747: (0xE036, 4, 0, 4, 0),  # AssignableButtonIndicator2
    0x0748: (0xE037, 4, 0, 4, 0),  # AssignableButtonIndicator3
    0x0749: (0xE038, 4, 0, 4, 0),  # AssignableButtonIndicator4
    0x074A: (0xE039, 4, 0, 4, 0),  # AssignableButtonIndicator5
    0x074B: (0xE03A, 4, 0, 4, 0),  # AssignableButtonIndicator6
    0x074C: (0xE03B, 4, 0, 4, 0),  # AssignableButtonIndicator7
    0x074D: (0xE03C, 4, 0, 4, 0),  # AssignableButtonIndicator8
    0x074E: (0xE03D, 4, 0, 4, 0),  # AssignableButtonIndicator9
    0x077B: (0xE03E, 4, 0, 4, 0),  # AssignableButtonIndicator10
    0x077C: (0xE08F, 4, 0, 4, 0),  # AssignableButtonIndicator11
    0x074F: (0xE03F, 4, 0, 4, 0),  # LensAssignableButtonIndicator1
    0x0750: (0xD01F, 4, 0, 4, 0),  # GaindBCurrentValue
    0x0751: (0xD040, 4, 0, 4, 0),  # SoftwareVersion
    0x0752: (0xE020, 4, 0, 4, 0),  # CurrentSceneFileEdited
    0x0753: (0xE061, 4, 0, 4, 0),  # MovieRecButtonToggleEnableStatus
    0x0754: (0xD284, 4, 0, 4, 0),  # RemoteTouchOperationEnableStatus
    0x0755: (0xD285, 4, 0, 4, 0),  # CancelRemoteTouchOperationEnableStatus
    0x0756: (0xE086, 4, 0, 4, 0),  # LensInformationEnableStatus
    0x0757: (0xE089, 4, 0, 4, 0),  # FollowFocusPositionCurrentValue
    0x0758: (0xD0AB, 4, 0, 4, 0),  # FocusBracketShootingStatus
    0x0759: (0xD0C6, 4, 0, 4, 0),  # PixelMappingEnableStatus
    0x075A: (0xD104, 4, 0, 4, 0),  # TimeCodePresetResetEnableStatus
    0x075B: (0xD105, 4, 0, 4, 0),  # UserBitPresetResetEnableStatus
    0x075C: (0xD106, 4, 0, 4, 0),  # SensorCleaningEnableStatus
    0x075D: (0xD107, 4, 0, 4, 0),  # PictureProfileResetEnableStatus
    0x075E: (0xD108, 4, 0, 4, 0),  # CreativeLookResetEnableStatus
    0x075F: (0xD07D, 4, 0, 4, 0),  # LensVersionNumber
    0x0760: (0xD251, 4, 0, 4, 0),  # DeviceOverheatingState
    0x0761: (0xD11F, 4, 0, 4, 0),  # Movie_IntervalRec_CountDownIntervalTime
    0x0762: (0xD120, 4, 0, 4, 0),  # Movie_IntervalRec_RecordingDuration
    0x0763: (0xD282, 4, 0, 4, 0),  # HighResolutionShutterSpeed
    0x0764: (0xD08B, 4, 0, 4, 0),  # BaseLookImportOperationEnableStatus
    0x0765: (0xD07B, 4, 0, 4, 0),  # LensModelName
    0x0766: (0xE043, 4, 0, 4, 0),  # FocusPositionCurrentValue
    0x0767: (0xD19C, 4, 0, 4, 0),  # FocusDrivingStatus
    0x0768: (0xD2BA, 4, 0, 4, 0),  # FlickerScanStatus
    0x0769: (0xD2BB, 4, 0, 4, 0),  # FlickerScanEnableStatus
    0x076B: (0xD09A, 4, 0, 4, 0),  # FTPServerSettingOperationEnableStatus
    0x076C: (0xD274, 4, 0, 4, 0),  # FTPTransferSetting_SaveOperationEnableStatus
    0x076D: (0xD275, 4, 0, 4, 0),  # FTPTransferSetting_ReadOperationEnableStatus
    0x076E: (0xD276, 4, 0, 4, 0),  # FTPTransferSetting_SaveRead_State
    0x0770: (0xD194, 4, 0, 4, 0),  # CameraShakeStatus
    0x0771: (0xD195, 4, 0, 4, 0),  # UpdateBodyStatus
    0x0773: (0xD197, 4, 0, 4, 0),  # MediaSLOT1_WritingState
    0x0774: (0xD198, 4, 0, 4, 0),  # MediaSLOT2_WritingState
    0x0776: (0xD02B, 4, 0, 4, 0),  # MediaSLOT1_RecordingAvailableType
    0x0777: (0xD02C, 4, 0, 4, 0),  # MediaSLOT2_RecordingAvailableType
    0x0778: (0xD190, 4, 0, 4, 0),  # MediaSLOT3_RecordingAvailableType
    0x0779: (0xD0BC, 4, 0, 4, 0),  # CameraOperatingMode
    0x077A: (0xD0BD, 4, 0, 4, 0),  # PlaybackViewMode
    0x0781: (0xD18E, 4, 0, 4, 0),  # MediaSLOT3_Status
    0x0783: (0xD18F, 4, 0, 4, 0),  # MediaSLOT3_RemainingTime
    0x0786: (0xE098, 4, 0, 4, 0),  # MonitoringDeliveringStatus
    0x0787: (0xE099, 4, 0, 4, 0),  # MonitoringIsDelivering
    0x0788: (0xE09D, 4, 0, 4, 0),  # MonitoringSettingVersion
    0x0789: (0xE09F, 4, 0, 4, 0),  # MonitoringDeliveryTypeSupportInfo
    0x078B: (0xD1BB, 4, 0, 4, 0),  # CameraErrorCautionStatus
    0x078C: (0xD1BC, 4, 0, 4, 0),  # SystemErrorCautionStatus
    0x078D: (0xD20C, 4, 0, 4, 0),  # CameraButtonFunctionStatus
    0x078E: (0xD134, 4, 0, 4, 0),  # FlickerLessShootingStatus
    0x078F: (0xD130, 4, 0, 4, 0),  # ContinuousShootingSpotBoostStatus
    0x0790: (0xD131, 4, 0, 4, 0),  # ContinuousShootingSpotBoostEnableStatus
    0x0791: (0xD19B, 4, 0, 4, 0),  # TimeShiftShootingStatus
    0x0792: (0xD19D, 4, 0, 4, 0),  # ZoomDrivingStatus
    0x0793: (0xD1B4, 4, 0, 4, 0),  # ShootingSelfTimerStatus
    0x0794: (0xD1DB, 4, 0, 4, 0),  # CreateNewFolderEnableStatus
    0x0795: (0xD1C9, 4, 0, 4, 0),  # ForcedFileNumberResetEnableStatus
    0x0796: (0xD19E, 4, 0, 4, 0),  # DefaultAFFreeSizeAndPositionSetting
    0x0797: (0xD1C6, 4, 0, 4, 0),  # TrackingOnAndAFOnEnableStatus
    0x0798: (0xD1BF, 4, 0, 4, 0),  # ProgramShiftStatus
    0x0799: (0xD1B5, 4, 0, 4, 0),  # MeteredManualLevel
    0x079B: (0xD12D, 4, 0, 4, 0),  # SecondBatteryRemain
    0x079C: (0xD12E, 4, 0, 4, 0),  # SecondBatteryLevel
    0x079D: (0xD204, 4, 0, 4, 0),  # TotalBatteryRemain
    0x079E: (0xD205, 4, 0, 4, 0),  # TotalBatteryLevel
    0x028D: (0xD20B, 3, 0, 3, 0),  # CameraLeverFunction
    0x028E: (0xD202, 1, 0, 2, 0),  # ShootingTimingPreNotificationMode
    0x028F: (0xD1DD, 1, 0, 4, 0),  # MicrophoneDirectivity
    0x0290: (0xD1DF, 1, 0, 2, 0),  # ProductShowcaseSet
    0x0291: (0xD1E0, 0, 0, 0, 0),  # AmountOfDefocusSetting
    0x0292: (0xD1E1, 1, 0, 2, 0),  # CinematicVlogSetting
    0x0293: (0xD1E2, 3, 0, 3, 0),  # CinematicVlogLook
    0x0294: (0xD1E3, 1, 0, 4, 0),  # CinematicVlogMood
    0x0295: (0xD1E4, 1, 0, 3, 0),  # CinematicVlogAFTransitionSpeed
    0x07A2: (0xE0A1, 4, 0, 4, 0),  # MonitoringTransportProtocol
    0x07A3: (0xE0A2, 4, 0, 4, 0),  # MonitoringAvailableFormat
    0x07A4: (0xE0A3, 4, 0, 4, 0),  # MonitoringFormatSupportInformation
    0x02BB: (0xE0A4, 2, 0, 2, 0),  # DeSqueezeDisplayRatio
    0x02BC: (0xE040, 0, 0, 0, 0),  # ZoomPositionSetting
    0x07A1: (0xE041, 4, 0, 4, 0),  # ZoomPositionCurrentValue
    0x0F07: (0xE0CF, 4, 0, 4, 0),
    0x0F08: (0xE0D0, 4, 0, 4, 0),
    0x0F09: (0xE0D1, 4, 0, 4, 0),
    0x0F0A: (0xD2B4, 4, 0, 4, 0),
    0x0F0C: (0xE0B3, 4, 0, 4, 0),
    0x0296: (0xD078, 1, 0, 2, 0),  # MonitoringOutputDisplaySDI
    0x07AC: (0xD07A, 4, 0, 4, 0),  # CameraSystemErrorInfo
    0x0297: (0xE079, 3, 0, 3, 0),  # AFAreaPositionAF_C
    0x0298: (0xE078, 3, 0, 3, 0),  # AFAreaPositionAF_S
    0x07AD: (0xD09B, 4, 0, 4, 0),  # FaceEyeDetectionAFStatus
    0x0299: (0xD091, 1, 0, 2, 0),  # AutoFocusHold
    0x029A: (0xD06E, 1, 0, 2, 0),  # PushAFModeSetting
    0x029B: (0xD064, 1, 0, 2, 0),  # TouchFunctionInMF
    0x029C: (0xD05E, 1, 0, 2, 0),  # PushAutoFocus
    0x029D: (0xD05C, 1, 0, 2, 0),  # PushAGC
    0x029E: (0xD05B, 1, 0, 2, 0),  # PushAutoIris
    0x02A3: (0xD077, 2, 0, 2, 0),  # NDFilterPreset3Value
    0x02A2: (0xD076, 2, 0, 2, 0),  # NDFilterPreset2Value
    0x02A1: (0xD075, 2, 0, 2, 0),  # NDFilterPreset1Value
    0x02A0: (0xD074, 1, 0, 3, 0),  # NDFilterPresetSelect
    0x029F: (0xD05D, 1, 0, 2, 0),  # PushAutoNDFilter
    0x02AB: (0xD0AA, 0, 0, 0, 0),  # WhiteBalanceOffsetColorTemp
    0x02AA: (0xD0A9, 1, 0, 2, 0),  # WhiteBalanceOffsetSetting
    0x02A9: (0xD08A, 0, 0, 0, 0),  # WhiteBalanceOffsetTintATW
    0x02A8: (0xD089, 0, 0, 0, 0),  # WhiteBalanceOffsetColorTempATW
    0x02A7: (0xD088, 0, 0, 0, 0),  # WhiteBalanceBGain
    0x02A6: (0xD087, 0, 0, 0, 0),  # WhiteBalanceRGain
    0x02A5: (0xD086, 0, 0, 0, 0),  # WhiteBalancePresetColorTemperature
    0x02A4: (0xD085, 1, 0, 3, 0),  # WhiteBalanceSwitch
    0x02B4: (0xD06D, 0, 0, 0, 0),  # PaintLookDetailLevel
    0x02B3: (0xD06C, 1, 0, 2, 0),  # PaintLookDetailSetting
    0x02B2: (0xD06B, 0, 0, 0, 0),  # PaintLookKneeSlope
    0x02B1: (0xD06A, 0, 0, 0, 0),  # PaintLookKneePoint
    0x02B0: (0xD069, 1, 0, 2, 0),  # PaintLookAutoKnee
    0x02AF: (0xD068, 1, 0, 2, 0),  # PaintLookKneeSetting
    0x02AE: (0xD067, 0, 0, 0, 0),  # PaintLookBBlack
    0x02AD: (0xD066, 0, 0, 0, 0),  # PaintLookRBlack
    0x02AC: (0xD065, 0, 0, 0, 0),  # PaintLookMasterBlack
    0x07AE: (0xD057, 4, 0, 4, 0),  # UploadDatasetVersion
    0x02B5: (0xD2B1, 3, 0, 3, 0),  # UserBaseLookOutput
    0x07AF: (0xD2A9, 4, 0, 4, 0),  # MonitorLUTSettingOutputDestAssign
    0x02B6: (0xD2AA, 1, 0, 2, 0),  # MonitorLUTSetting1
    0x02B7: (0xD2AB, 1, 0, 2, 0),  # MonitorLUTSetting2
    0x02B8: (0xD2AC, 1, 0, 2, 0),  # MonitorLUTSetting3
    0x07B0: (0xD0C1, 4, 0, 4, 0),  # MaximumNumberOfBytes
    0x02B9: (0xD051, 1, 0, 2, 0),  # SQModeSetting
    0x02BA: (0xE0A0, 1, 0, 2, 0),  # MovieQualityFullAutoMode
    0x02BD: (0xD1D0, 1, 0, 26, 0),  # FileSettingsCameraId
    0x02BE: (0xD1D1, 0, 0, 0, 0),  # FileSettingsReelNumber
    0x02BF: (0xD1D2, 1, 0, 3, 0),  # FileSettingsCameraPosition
    0x02C0: (0xD1A9, 1, 0, 3, 0),  # ImageStabilizationFramingStabilizer
    0x02C1: (0xD237, 2, 0, 2, 0),  # ExposureStep
    0x07A0: (0xD2BD, 4, 0, 4, 0),  # TeleWideLeverValueCapability
    0x02C2: (0xE0CD, 1, 0, 2, 0),  # EnlargeScreenSetting
    0x07A5: (0xD1D4, 4, 0, 4, 0),  # MediaSLOT1_ContentsInfoListEnableStatus
    0x07A6: (0xD1D5, 4, 0, 4, 0),  # MediaSLOT2_ContentsInfoListEnableStatus
    0x07A7: (0xD1D6, 4, 0, 4, 0),  # MediaSLOT1_ContentsInfoListRegenerateUpdateTime
    0x07A8: (0xD1D7, 4, 0, 4, 0),  # MediaSLOT2_ContentsInfoListRegenerateUpdateTime
    0x07A9: (0xE0D9, 4, 0, 4, 0),  # MediaSLOT1_ContentsInfoListUpdateTime
    0x07AA: (0xE0DA, 4, 0, 4, 0),  # MediaSLOT2_ContentsInfoListUpdateTime
    0x07AB: (0xD1DA, 4, 0, 4, 0),  # PostViewTransferResourceStatus
    0x02C3: (0xD050, 1, 0, 2, 0),  # SimulRecSetting
    0x02C4: (0xD07F, 1, 0, 3, 0),  # SimulRecSettingMovieRecButton
    0x02C9: (0xD012, 1, 0, 2, 0),  # ShutterSelectMode
    0x02C5: (0xD207, 3, 0, 3, 0),  # OSDImageMode
    0x07B1: (0xD0BF, 4, 0, 4, 0),  # FirmwareUpdateCommandVersion
    0x02C6: (0xE0D5, 1, 0, 2, 0),  # DebugMode
    0x0F0B: (0xD0C0, 4, 0, 4, 0),
    0x02C7: (0xE0DF, 1, 0, 2, 0),  # reserved18
    0x02C8: (0xE0E0, 3, 0, 3, 0),  # reserved19
    0x0F0D: (0xE0C0, 4, 0, 4, 0),
    0x07B5: (0xE0CC, 4, 0, 4, 0),  # SetPresetPTZFBinaryVersion
    0x07B6: (0xE0B7, 4, 0, 4, 0),  # PanPositionStatus
    0x07B7: (0xE0B9, 4, 0, 4, 0),  # TiltPositionStatus
    0x07B8: (0xE0B6, 4, 0, 4, 0),  # PanPositionCurrentValue
    0x07B9: (0xE0B8, 4, 0, 4, 0),  # TiltPositionCurrentValue
    0x02CB: (0xE05C, 2, 0, 2, 0),  # PanTiltAccelerationRampCurve
    0x02CC: (0xE0BE, 1, 0, 2, 0),  # PanLimitMode
    0x02CD: (0xE0BA, 0, 0, 0, 0),  # PanLimitRangeMinimum
    0x02CE: (0xE0BB, 0, 0, 0, 0),  # PanLimitRangeMaximum
    0x02CF: (0xE0BF, 1, 0, 2, 0),  # TiltLimitMode
    0x02D0: (0xE0BC, 0, 0, 0, 0),  # TiltLimitRangeMinimum
    0x02D1: (0xE0BD, 0, 0, 0, 0),  # TiltLimitRangeMaximum
    0x02D2: (0xE0CB, 3, 0, 3, 0),  # PresetPTZFSlotNumber
    0x07BA: (0xE0AF, 4, 0, 4, 0),  # CameraPowerStatus
    0x0313: (0xD2BE, 1, 0, 16, 0),  # TargetStreamingDestinationSelect
    0x07CD: (0xD119, 4, 0, 4, 0),  # StreamStatus
    0x02D3: (0xE0A5, 1, 0, 2, 0),  # IRRemoteSetting
    0x02D4: (0xE0A6, 1, 0, 2, 0),  # IPSetupProtocolSetting
    0x07BB: (0xE0B0, 4, 0, 4, 0),  # RecordablePowerSources
    0x07CF: (0xD1CC, 4, 0, 4, 0),  # StreamSettingListOperationStatus
    0x02E4: (0xD29E, 1, 0, 2, 0),  # PaintLookMultiMatrixAreaIndication
    0x02D5: (0xD002, 1, 0, 2, 0),  # IrisCloseSetting
    0x07BC: (0xD080, 4, 0, 4, 0),  # DisplayedMenuStatus
    0x02D6: (0xD08F, 1, 0, 24, 0),  # LanguageSetting
    0x07BD: (0xD09C, 4, 0, 4, 0),  # PlaybackContentsRecordingDateTime
    0x07BE: (0xD09D, 4, 0, 4, 0),  # PlaybackContentsName
    0x07BF: (0xD09E, 4, 0, 4, 0),  # PlaybackContentsNumber
    0x07C0: (0xD09F, 4, 0, 4, 0),  # PlaybackContentsTotalNumber
    0x07C1: (0xD0A0, 4, 0, 4, 0),  # PlaybackContentsRecordingResolution
    0x07C2: (0xD0A1, 4, 0, 4, 0),  # PlaybackContentsRecordingFrameRate
    0x07C3: (0xD0A2, 4, 0, 4, 0),  # PlaybackContentsRecordingFileFormat
    0x07C4: (0xD0A4, 4, 0, 4, 0),  # PlaybackContentsGammaType
    0x07C5: (0xD0C3, 4, 0, 4, 0),  # BaseLookNameofPlayback
    0x07C6: (0xD0C4, 4, 0, 4, 0),  # BaseLookAppliedofPlayback
    0x02D7: (0xD139, 1, 0, 2, 0),  # PaintLookUserMatrixSetting
    0x02D8: (0xD13A, 0, 0, 0, 0),  # PaintLookUserMatrixLevel
    0x02D9: (0xD13B, 0, 0, 0, 0),  # PaintLookUserMatrixPhase
    0x02DA: (0xD13C, 0, 0, 0, 0),  # PaintLookUserMatrixRG
    0x02DB: (0xD13D, 0, 0, 0, 0),  # PaintLookUserMatrixRB
    0x02DC: (0xD13E, 0, 0, 0, 0),  # PaintLookUserMatrixGR
    0x02DD: (0xD13F, 0, 0, 0, 0),  # PaintLookUserMatrixGB
    0x02DE: (0xD140, 0, 0, 0, 0),  # PaintLookUserMatrixBR
    0x02DF: (0xD141, 0, 0, 0, 0),  # PaintLookUserMatrixBG
    0x02E0: (0xD142, 1, 0, 2, 0),  # PaintLookMultiMatrixSetting
    0x02E1: (0xD143, 3, 0, 3, 0),  # PaintLookMultiMatrixAxis
    0x02E2: (0xD144, 0, 0, 0, 0),  # PaintLookMultiMatrixHue
    0x02E3: (0xD145, 0, 0, 0, 0),  # PaintLookMultiMatrixSaturation
    0x07C7: (0xD2AE, 4, 0, 4, 0),  # MonitoringOutputDisplaySettingDestAssign
    0x02FC: (0xD2AF, 1, 0, 2, 0),  # MonitoringOutputDisplaySetting1
    0x02FD: (0xD2B0, 1, 0, 2, 0),  # MonitoringOutputDisplaySetting2
    0x07C8: (0xE044, 4, 0, 4, 0),  # FocusModeStatus
    0x07C9: (0xE045, 4, 0, 4, 0),  # FocusOperationWithInt16EnableStatus
    0x02E5: (0xE048, 1, 0, 2, 0),  # AudioInputCH1LevelControl
    0x02E6: (0xE049, 1, 0, 2, 0),  # AudioInputCH2LevelControl
    0x02E7: (0xE04A, 1, 0, 2, 0),  # AudioInputCH3LevelControl
    0x02E8: (0xE04B, 1, 0, 2, 0),  # AudioInputCH4LevelControl
    0x02E9: (0xE04C, 0, 0, 0, 0),  # AudioInputCH1Level
    0x02EA: (0xE04D, 0, 0, 0, 0),  # AudioInputCH2Level
    0x02EB: (0xE04E, 0, 0, 0, 0),  # AudioInputCH3Level
    0x02EC: (0xE04F, 0, 0, 0, 0),  # AudioInputCH4Level
    0x02ED: (0xE051, 1, 0, 8, 0),  # AudioInputCH1InputSelect
    0x02EE: (0xE052, 1, 0, 8, 0),  # AudioInputCH2InputSelect
    0x02EF: (0xE053, 1, 0, 8, 0),  # AudioInputCH3InputSelect
    0x02F0: (0xE054, 1, 0, 8, 0),  # AudioInputCH4InputSelect
    0x02F1: (0xE055, 1, 0, 2, 0),  # AudioInputCH1WindFilter
    0x02F2: (0xE056, 1, 0, 2, 0),  # AudioInputCH2WindFilter
    0x02F3: (0xE057, 1, 0, 2, 0),  # AudioInputCH3WindFilter
    0x02F4: (0xE058, 1, 0, 2, 0),  # AudioInputCH4WindFilter
    0x02F7: (0xE05F, 1, 0, 2, 0),  # RemoteKeyThumbnailButton
    0x02F8: (0xE060, 1, 0, 2, 0),  # RemoteKeySLOTSelectButton
    0x02F9: (0xE067, 3, 0, 3, 0),  # VideoRecordingFormatBitrateSetting
    0x07CA: (0xE068, 4, 0, 4, 0),  # ValidRecordingVideoFormat
    0x02FB: (0xE06C, 2, 0, 2, 0),  # MonitoringOutputFormat
    0x02FE: (0xE092, 0, 0, 0, 0),  # FocusSpeedDirectSync
    0x02F5: (0xE0AA, 1, 0, 2, 0),  # AudioInput1TypeSelect
    0x02F6: (0xE0AB, 1, 0, 2, 0),  # AudioInput2TypeSelect
    0x02FA: (0xE0B5, 1, 0, 3, 0),  # VideoRecordingFormatQuality
    0x02FF: (0xE0CE, 0, 0, 0, 0),  # LiveViewImageQualityByNumericalValue
    0x0300: (0xE0D2, 1, 0, 2, 0),  # TallyLampControlRed
    0x0301: (0xE0D3, 1, 0, 2, 0),  # TallyLampControlGreen
    0x0302: (0xE0D4, 1, 0, 2, 0),  # TallyLampControlYellow
    0x0305: (0xD026, 2, 0, 2, 0),  # Movie_RecordingResolutionForRTSP
    0x0307: (0xD02D, 3, 0, 3, 0),  # Movie_RecordingFrameRateRTSPSetting
    0x0308: (0xD053, 1, 0, 2, 0),  # PictureCacheRecSetting
    0x0309: (0xD054, 2, 0, 2, 0),  # PictureCacheRecSizeAndTime
    0x030A: (0xD056, 2, 0, 2, 0),  # Movie_IntervalRecFrames
    0x030B: (0xD05F, 1, 0, 3, 0),  # ImagerScanMode
    0x0306: (0xD063, 2, 0, 2, 0),  # Movie_RecordingResolutionForRAW
    0x07CB: (0xD07C, 4, 0, 4, 0),  # LensSerialNumber
    0x030C: (0xE0FA, 1, 0, 2, 0),  # ShootingEnableSettingLicense
    0x030D: (0xE10E, 1, 0, 2, 0),  # GridLineDisplayPlayback
    0x030E: (0xE10F, 3, 0, 3, 0),  # GridLineType
    0x07D9: (0xE110, 4, 0, 4, 0),  # CustomGridLineFileCommandVersion
    0x07CC: (0xE0FE, 4, 0, 4, 0),  # MaximumSizeOfImageIDString
    0x07CE: (0xE112, 4, 0, 4, 0),  # StreamButtonEnableStatus
    0x07B3: (0xD229, 4, 0, 4, 0),  # AutoRecognitionTargetCandidates
    0x02CA: (0xD234, 0, 0, 0, 0),  # AutoRecognitionTargetSetting
    0x07D3: (0xE0F3, 4, 0, 4, 0),  # DeleteContentOperationEnableStatusSLOT1
    0x07D4: (0xE0F4, 4, 0, 4, 0),  # DeleteContentOperationEnableStatusSLOT2
    0x030F: (0xE0F5, 1, 0, 2, 0),  # DifferentSetForSQMovie
    0x0310: (0xE0E2, 2, 0, 2, 0),  # ManualInputForNDFilterValue
    0x0311: (0xE0E3, 3, 0, 3, 0),  # LogShootingMode
    0x0312: (0xE0E4, 1, 0, 2, 0),  # LogShootingModeColorGamut
    0x0315: (0xD0AC, 1, 0, 16, 0),  # VideoStreamSelect
    0x0314: (0xD2BF, 1, 0, 1, 0),  # StreamDisplayName
    0x0316: (0xD0AE, 2, 0, 2, 0),  # VideoStreamResolution
    0x0317: (0xD2C0, 0, 0, 0, 0),  # VideoStreamMaxBitRate
    0x0318: (0xD10E, 1, 0, 2, 0),  # VideoStreamAdaptiveRateControl
    0x0319: (0xD0AD, 1, 0, 4, 0),  # VideoStreamCodec
    0x031A: (0xD116, 0, 0, 0, 0),  # StreamLatency
    0x031B: (0xD117, 0, 0, 0, 0),  # StreamTTL
    0x031C: (0xD113, 1, 0, 4, 0),  # StreamCipherType
    0x031D: (0xD118, 1, 0, 4, 0),  # StreamModeSetting
    0x031E: (0xD10F, 1, 0, 2, 0),  # VideoStreamResolutionMethod
    0x031F: (0xD11A, 1, 0, 2, 0),  # VideoStreamMovieRecPermission
    0x0320: (0xD0B5, 1, 0, 2, 0),  # VideoStreamBitRateCompressionMode
    0x0321: (0xD2B3, 1, 0, 2, 0),  # VideoStreamBitRateVBRMode
    0x0322: (0xD11B, 32, 0, 32, 0),  # AudioStreamCodecType
    0x0323: (0xD11C, 2, 0, 2, 0),  # AudioStreamSamplingFrequency
    0x0324: (0xD11D, 1, 0, 3, 0),  # AudioStreamBitDepth
    0x0325: (0xD11E, 3, 0, 3, 0),  # AudioStreamChannel
    0x0326: (0xE111, 1, 0, 2, 0),  # HomeMenuSetting
    0x0327: (0xE0E1, 1, 0, 2, 0),  # CallSetting
    0x0328: (0xE0E5, 0, 0, 0, 0),  # NDFilterPositionSetting
    0x07D5: (0xE0E6, 4, 0, 4, 0),  # SceneFileCommandVersion
    0x07D6: (0xE101, 4, 0, 4, 0),  # SceneFileUploadOperationEnableStatus
    0x07D7: (0xE102, 4, 0, 4, 0),  # SceneFileDownloadOperationEnableStatus
    0x07D8: (0xE0F9, 4, 0, 4, 0),  # SceneFileIndexesAvailableForDownload
    0x07D1: (0xD122, 4, 0, 4, 0),  # EframingType
    0x07D2: (0xD123, 4, 0, 4, 0),  # EframingCommandVersion
    0x0329: (0xE0F8, 1, 0, 2, 0),  # EframingAutoFraming
    0x032A: (0xE0F0, 1, 0, 2, 0),  # EframingTrackingStartMode
    0x032B: (0xE0F1, 1, 0, 3, 0),  # EframingProductionEffect
    0x032C: (0xD127, 0, 0, 0, 0),  # EframingSpeedPTZ
    0x0601: (0xD009, 0, 0, 0, 0),
    0x0331: (0xD18C, 3, 0, 3, 0),  # TopOfTheGroupShootingMarkSetting
    0x0603: (0xD18D, 0, 0, 5, 0),
    0x0332: (0xD148, 1, 0, 2, 0),  # CompRAWShootingNR
    0x0333: (0xD149, 3, 0, 3, 0),  # CompRAWShootingNRFileCompressionType
    0x0334: (0xD15A, 2, 0, 2, 0),  # CompRAWShootingNRNumberOfSheets
    0x07DA: (0xD2A6, 4, 0, 4, 0),  # ElapsedBulbExposureTime
    0x07DB: (0xD2A7, 4, 0, 4, 0),  # RemainingBulbExposureTime
    0x07DC: (0xD2A8, 4, 0, 4, 0),  # RemainingNoiseReductionTime
    0x0F01: (0xD261, 4, 0, 4, 0),
    0x0F02: (0xD22A, 4, 0, 4, 0),
    0x032D: (0xE100, 2, 0, 2, 0),  # DigitalExtenderMagnificationSetting
    0x032E: (0xE07A, 0, 0, 1, 0),  # MovieRecReviewPlayingState
    0x011F: (0xD2D1, 3, 0, 3, 0),  # NearFar
    0x0120: (0xD2D2, 3, 0, 3, 0),  # reserved7
    0x0121: (0xD2DC, 3, 0, 3, 0),  # AF_Area_Position
    0x0126: (0xD2DD, 3, 0, 3, 0),  # Zoom_Operation
    0x0134: (0xD2E9, 3, 0, 3, 0),  # ZoomAndFocusPosition_Save
    0x0135: (0xD2EA, 3, 0, 3, 0),  # ZoomAndFocusPosition_Load
    0x015B: (0xD2EC, 3, 0, 3, 0),  # ColortempStep
    0x015E: (0xD2ED, 3, 0, 3, 0),  # WhiteBalanceTintStep
    0x015F: (0xD2EF, 3, 0, 3, 0),  # Focus_Operation
    0x0162: (0xF000, 3, 0, 3, 0),  # ShutterECSNumberStep
    0x0193: (0xD2E4, 3, 0, 3, 0),  # RemoteTouchOperation
    0x027C: (0xD2F2, 3, 0, 3, 0),  # ZoomAndFocusPresetZoomOnly_Set
    0x0509: (0xD2DF, 3, 0, 3, 0),  # CustomWB_Capture_Standby
    0x050A: (0xD2E0, 3, 0, 3, 0),  # CustomWB_Capture_Standby_Cancel
    0x050B: (0xD2E1, 3, 0, 3, 0),  # CustomWB_Capture
    0x0303: (0xF003, 3, 0, 3, 0),  # ZoomOperationWithInt16
    0x0304: (0xF004, 3, 0, 3, 0),  # FocusOperationWithInt16
    0x032F: (0xD2E3, 3, 0, 3, 0),  # HighResolutionShutterSpeedAdjust
    0x0330: (0xD2F0, 3, 0, 3, 0),  # HighResolutionShutterSpeedAdjustInIntegralMultiples
    0x034B: (0xE0F6, 1, 0, 2, 0),  # Movie_AngleOfViewPriority
    0x034C: (0xE0D6, 1, 0, 2, 0),  # WindNoiseReductForExternalMic
    0x034D: (0xE0D7, 1, 0, 2, 0),  # NoiseCutFilter
    0x034E: (0xE0D8, 1, 0, 2, 0),  # NoiseCutFilterForExternalMic
    0x07DD: (0xE107, 4, 0, 4, 0),  # DispModeCandidateStill
    0x0339: (0xE108, 0, 0, 0, 0),  # DispModeSettingStill
    0x033A: (0xE109, 1, 0, 8, 0),  # DispModeStill
    0x07DE: (0xE10A, 4, 0, 4, 0),  # DispModeCandidateMovie
    0x033B: (0xE10B, 0, 0, 0, 0),  # DispModeSettingMovie
    0x033C: (0xE10C, 1, 0, 8, 0),  # DispModeMovie
    0x0335: (0xE0DB, 1, 0, 2, 0),  # CompRAWShootingHDR
    0x0338: (0xE0DC, 3, 0, 3, 0),  # CompRAWShootingHDRDRSetting
    0x0336: (0xE0DD, 3, 0, 3, 0),  # CompRAWShootingHDRFileCompressionType
    0x0337: (0xE0DE, 2, 0, 2, 0),  # CompRAWShootingHDRNumberOfSheets
    0x07DF: (0xE081, 4, 0, 4, 0),  # ControlGeneralSettingFileEnableStatus
    0x033D: (0xE11A, 1, 0, 2, 0),  # PeakingDisplay
    0x033E: (0xE11B, 1, 0, 3, 0),  # PeakingLevel
    0x033F: (0xE11C, 1, 0, 4, 0),  # PeakingColor
    0x0340: (0xE11D, 1, 0, 2, 0),  # ZebraDisplay
    0x0341: (0xE11E, 2, 0, 2, 0),  # ZebraLevel
    0x0342: (0xE11F, 1, 0, 2, 0),  # ZebraLevelTypeCustom
    0x0343: (0xE120, 0, 0, 0, 0),  # ZebraLevelStandardCustom
    0x0344: (0xE121, 0, 0, 0, 0),  # ZebraLevelRangeCustom
    0x0345: (0xE122, 0, 0, 0, 0),  # ZebraLevelLowerLimitCustom
    0x0346: (0xE123, 1, 0, 2, 0),  # MarkerDisplay
    0x0347: (0xE124, 1, 0, 2, 0),  # CenterMarkerDisplay
    0x0348: (0xE125, 1, 0, 16, 0),  # AspectMarkerRatioMovie
    0x0349: (0xE126, 2, 0, 2, 0),  # SafetyZoneDisplay
    0x034A: (0xE127, 1, 0, 2, 0),  # GuideframeDisplay
    0x034F: (0xE12A, 1, 0, 2, 0),  # DualGain
    0x0350: (0xE131, 2, 0, 2, 0),  # ImagerMode
    0x0351: (0xE133, 1, 0, 2, 0),  # DisplayQualityForFinderOnly
    0x0352: (0xE134, 1, 0, 2, 0),  # DisplayQualityForMonitorOnly
    0x0F06: (0xD264, 4, 0, 4, 0),
    0x0602: (0xD1C2, 0, 0, 2, 0),
    0x0F03: (0xD1C3, 4, 0, 4, 0),
    0x0F04: (0xD1C4, 4, 0, 4, 0),
    0x0F05: (0xD1C5, 4, 0, 4, 0),
}
