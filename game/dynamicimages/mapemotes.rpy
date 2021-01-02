init python:
#Dynamic Sprite System-Each category represents a folder in the Images section. These will be auto-defined.
   # Automatically define the BGs, CGs, and some UI elements
   DefineImages('cgs')
   DefineImages('bgs', prepend='bg')
   DefineImages('mainmenu', prepend='mm')
   # define the composite sprites with LayeredImages, blinking eyes and flapping mouth
   DefineImages("sprites", composite=True)

   layerorder = ['hair', 'base', 'arms', 'tail','mouth','eyes','brow','blush']
   DefineImages('images/sprites', composite=True, overrideLayerOrder=layerorder, offsets=(0, 100), zooms={'Kan':.85,'Rin':.85,'Kyou':.85, 'Maya': .85, 'Youk':.85, 'Char':.7}, sides=['Kan', 'Rin', 'Kyou','Maya','Youk','Char'])

   #Dynamic Sprite Emote Maps
   #MapEmote('war hugesmile',  'war md_hugesmile ed_bigsmile blush')
   # override some default eye blink and mouth flap behaviours
   #image war_ed_default = BlinkEyes("war_e_default", "war_ec_grin")
   # image war_md_hugesmile = FlapMouth("war_mc_smug", "war_m_bigsmile")

####Kanna
   MapEmote('Kan smile worried eo', 'Kan base mdo_happy ed_default brow_sad')
   MapEmote('Kan smile worried ec', 'Kan base mdo_happy ec_happy brow_sad')
   MapEmote('Kan frown worried eo', 'Kan base md_frown ed_default brow_sad')
   MapEmote('Kan frown worried ec', 'Kan base md_frown ec_happy brow_sad')
   MapEmote('Kan speaking embarrassed ec', 'Kan base mdo_oh ec_happy brow_sad blush')
   MapEmote('Kan speaking excited crazy blush', 'Kan base mdo_oh ed_crazy brow_angry blush')
   MapEmote('Kan frown skeptic', 'Kan base md_frown ed_default brow_skeptic')
   MapEmote('Kan frown angry', 'Kan base md_frown ed_default brow_furrow')
   MapEmote('Kan frown confident ec', 'Kan base md_frown ec_default brow_angry')
   MapEmote('Kan frown pout ec', 'Kan base md_frown ec_default brow_default')
   MapEmote('Kan smile happy ec', 'Kan base md_smile ec_happy brow_content')
   MapEmote('Kan smile happy eo', 'Kan base mdo_happy ed_default brow_content')
   MapEmote('Kan smile happy blushing', 'Kan base mdo_happy ec_default brow_content blush')
   MapEmote('Kan smile happy speaking ec', 'Kan base mdo_happy ec_happy brow_content')
   MapEmote('Kan smile concerned ec', 'Kan base mdo_happy ec_happy brow_skeptic')
   MapEmote('Kan sleeping', 'Kan base mdo_oh ec_default brow_default')
   MapEmote('Kan neutral surprised crazy', 'Kan base md_frown ed_crazy brow_default')
   MapEmote('Kan smile surprised crazy', 'Kan base md_default ed_crazy brow_default')
   MapEmote('Kan speaking surprised crazy', 'Kan base mdo_oh ed_crazy brow_content')
   MapEmote('Kan speaking confident', 'Kan base mdo_oh ed_default brow_angry')
   MapEmote('Kan speaking pleading', 'Kan base mdo_oh ec_happy brow_angry')
   MapEmote('Kan speaking curious', 'Kan base mdo_oh ed_default brow_content')
   MapEmote('Kan speaking sarcastic ec', 'Kan base mdo_oh ec_default brow_content')
   MapEmote('Kan speaking skeptic eo', 'Kan base mdo_oh ed_crazy brow_skeptic')
   MapEmote('Kan drooling happy ec', 'Kan base mdo_drool ec_default brow_content')
   MapEmote('Kan drooling happy eo', 'Kan base mdo_drool ed_crazy brow_default blush')
   MapEmote('Kan speaking sad crazy', 'Kan base mdo_oh ed_crazy brow_sad')
   MapEmote('Kan salivating', 'Kan base mdo_drool ec_default brow_content blush')
   MapEmote('Kan questioning embarrassed', 'Kan base mdo_oh ec_happy brow_skeptic blush')
###Kyousuke
   MapEmote('Kyou normal', 'Kyou base md_default ed_default')
   MapEmote('Kyou smirk', 'Kyou base md_smirk ed_default')
   MapEmote('Kyou frown', 'Kyou base mdo_default ed_default')
   MapEmote('Kyou happy', 'Kyou base mdo_smile ed_default')

####Maya
   MapEmote('Maya smile happy mc', 'Maya base md_default ed_default brow_default')
   MapEmote('Maya smile happy mo', 'Maya base mdo_grin ed_default brow_default')
   MapEmote('Maya speaking normal', 'Maya base mdo_default ed_default brow_default')
   MapEmote('Maya sad speaking', 'Maya base mdo_default ec_default brow_furrow')
   MapEmote('Maya annoyed ec', 'Maya base mdo_default ec_default brow_scrunch')
   MapEmote('Maya annoyed eo', 'Maya base mdo_default ed_default brow_scrunch')
   MapEmote('Maya hopeless ec', 'Maya base md_default ec_default brow_furrow')