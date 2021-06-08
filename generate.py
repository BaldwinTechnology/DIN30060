#!/usr/bin/python
# -*- coding: utf-8 -*-
# simple .svg to .ttf icon font converter, (c) 2020 Baldi

# generate.py file taken from nipajin-dingbats

import fontforge, psMat

fontname = "DIN30600"
fullname = "DIN 30600 graphical symbols"
familyname = "DIN 30600"
version = "v1.1"
copyright = "Copyright (c) 2020, Baldi, Reserved Font Name \"DIN 30600\".\n\nThis Font Software is licensed under the SIL Open Font License, Version 1.1.\nThis license is available with a FAQ at: http://scripts.sil.org/OFL"

def getGlyphWidth(glyph):
    "determine width of a given glyph"
    box = glyph.boundingBox()
    return box[2] - box[0]

def getGlyphHeight(glyph):
    "determine height of a given glyph"
    box = glyph.boundingBox()
    return box[3] - box[1]

def addIcon( font, glyph, svgFileName, name="" ):
    "add a svg as icon glyph"
    glyph = font.createChar(glyph)
    glyph.importOutlines(svgFileName)

    if name == '':
        text = svgFileName[:-4]

        # "glyphs/DIN0003_Lesen_oder_Wiedergabe_von_einem_Informationstraeger.svg
        #  1...5...10....5...20
        text = text[15:] # alles, bis auf die ersten 15 Zeichen
        text = text.replace("_", " ")

        name = text
        #print (name)
    glyph.glyphname = name
    glyph.comment = name

    glyph.correctDirection()
    return;

def addDie( font, glyph, svgFileName, yOffset = 0 ):
    "add a svg as glyph (with a box)"
    scale = 0.75
    glyph = font.createChar(glyph)

    # get and store true width for later, as it will get distorted
    glyph.importOutlines("glyphs/_box.svg")
    width = glyph.width
    glyph.clear()

    # put icon in a die/box
    glyph.importOutlines(svgFileName)
    glyph.transform(psMat.scale(scale))
    glyph.transform(psMat.translate(1000 * (1 - scale) / 2, yOffset + 1000 * (1 - scale) / 2 - 200 * (1 - scale)))
    glyph.importOutlines("glyphs/_box.svg")
    glyph.correctDirection()

    glyph.width = width
    return;

def addCircle( font, glyph, svgFileName, yOffset = 0 ):
    "add a svg as glyph (with a circle)"
    scale = 0.75
    glyph = font.createChar(glyph)

    # get and store true width for later, as it will get distorted
    glyph.importOutlines("glyphs/_circle.svg")
    width = glyph.width
    glyph.clear()

    # put icon in a die/box
    glyph.importOutlines(svgFileName)
    glyph.transform(psMat.scale(scale))
    glyph.transform(psMat.translate(1000 * (1 - scale) / 2, yOffset + 1000 * (1 - scale) / 2 - 200 * (1 - scale)))
    glyph.importOutlines("glyphs/_circle.svg")
    glyph.correctDirection()

    glyph.width = width
    return;

# start with a new font
regular = fontforge.font()  # shape only
# bold    = fontforge.font()  # box shapes
# italic  = fontforge.font()  # circle shapes

# add some meta-data
regular.fontname = fontname + "-Regular"
regular.fullname = fullname
regular.familyname = familyname
regular.version = version
regular.copyright = copyright

# bold.fontname = fontname + "-Bold"
# bold.fullname = fullname + " Bold"
# bold.familyname = familyname
# bold.version = version
# bold.copyright = copyright

# italic.fontname = fontname + "-Italic"
# italic.fullname = fullname + " Italic"
# italic.familyname = familyname
# italic.version = version
# italic.copyright = copyright

# add symbols
# addIcon   (regular, ord('4'), "glyphs/d10.svg") // example

addIcon(regular,    3, "glyphs/DIN0003_Lesen_oder_Wiedergabe_von_einem_Informationstraeger.svg", "Lesen oder Wiedergabe von einem Informationsträger")
addIcon(regular,    4, "glyphs/DIN0004_Loeschen_einer_Information_von_einem_Informationstraeger.svg")
addIcon(regular,    9, "glyphs/DIN0009_Steuern.svg")
addIcon(regular,   10, "glyphs/DIN0010_Regeln.svg")
addIcon(regular,   11, "glyphs/DIN0011_Start_eines_Vorganges.svg")
addIcon(regular,   12, "glyphs/DIN0012_Schnellstart.svg")
addIcon(regular,   13, "glyphs/DIN0013_Stop_eines_Vorganges_Abbrechen.svg")
addIcon(regular,   14, "glyphs/DIN0014_Schnellstop.svg")
addIcon(regular,   15, "glyphs/DIN0015_Aus_Ausschalten_oder_Ausgeschaltet.svg")
addIcon(regular,   16, "glyphs/DIN0016_Ein_Einschalten_oder_Eingeschaltet.svg")
addIcon(regular,   17, "glyphs/DIN0017_Bereit.svg")
addIcon(regular,   18, "glyphs/DIN0018_Ein_Aus_Drucktaste_mit_zwei_festen_Stellungen.svg")
addIcon(regular,   19, "glyphs/DIN0019_Ein_Aus_Drucktaster.svg")
addIcon(regular,   20, "glyphs/DIN0020_Abschalten.svg")
addIcon(regular,   21, "glyphs/DIN0021_Zuschalten.svg")
addIcon(regular,   22, "glyphs/DIN0022_Bereitschaftsstellung_fuer_einen_Teil_des_Betriebsmittels.svg")
addIcon(regular,   23, "glyphs/DIN0023_Veraendern_einer_Groesse.svg")
addIcon(regular,   24, "glyphs/DIN0024_Maximaleinstellung.svg")
addIcon(regular,   25, "glyphs/DIN0025_Minimumeinstellung.svg")
addIcon(regular,   26, "glyphs/DIN0026_Eichen_Kalibrieren.svg")
addIcon(regular,   27, "glyphs/DIN0027_Aufnahme_auf_einen_Informationstraeger.svg")
addIcon(regular,   28, "glyphs/DIN0028_Bewegung_in_eine_Richtung.svg")
addIcon(regular,   29, "glyphs/DIN0029_Rueckuebertragung.svg")
addIcon(regular,   30, "glyphs/DIN0030_Nichtrechnen.svg")
addIcon(regular,   31, "glyphs/DIN0031_Zwischenresultat.svg")
addIcon(regular,   32, "glyphs/DIN0032_Resultat.svg")
addIcon(regular,   35, "glyphs/DIN0035_Handbetaetigung.svg")
addIcon(regular,   42, "glyphs/DIN0042_Elektrische_Maschine.svg")
addIcon(regular,   45, "glyphs/DIN0045_Entriegeln.svg")
addIcon(regular,   46, "glyphs/DIN0046_Verriegeln.svg")
addIcon(regular,   47, "glyphs/DIN0047_Zentrale_Schaltstelle.svg")
addIcon(regular,   56, "glyphs/DIN0056_Mittelstellung.svg")
addIcon(regular,   80, "glyphs/DIN0080_Zulaessige_Uebertemperatur.svg")
addIcon(regular,   82, "glyphs/DIN0082_Maschineninterne_Uebertragung_von_Daten.svg")
addIcon(regular,   84, "glyphs/DIN0084_Konstanten_Eingabe.svg")
addIcon(regular,   85, "glyphs/DIN0085_Konstanten_Abruf.svg")
addIcon(regular,   86, "glyphs/DIN0086_Gesamtloeschen_Gesamt_Nullstellen.svg")
addIcon(regular,   88, "glyphs/DIN0088_Maschinelles_Runden.svg")
addIcon(regular,   89, "glyphs/DIN0089_Schnelle_Bewegung_in_eine_Begrenzung.svg")
addIcon(regular,   90, "glyphs/DIN0090_Schnelle_Bewegung_aus_einer_Begrenzung.svg")
addIcon(regular,  100, "glyphs/DIN0100_Drehbewegung_nach_rechts.svg")
addIcon(regular,  101, "glyphs/DIN0101_Entfernungsringe.svg")
addIcon(regular,  102, "glyphs/DIN0102_Peilzeigereinstellung.svg")
addIcon(regular,  105, "glyphs/DIN0105_Taster_handbetaetigt.svg")
addIcon(regular,  111, "glyphs/DIN0111_Impulsmarkierung_auf_Informationstraeger.svg")
addIcon(regular,  112, "glyphs/DIN0112_Trennschnitt.svg")
addIcon(regular,  113, "glyphs/DIN0113_Pause_Unterbrechung.svg")
addIcon(regular,  114, "glyphs/DIN0114_Drehbewegung_nach_links.svg")
addIcon(regular,  115, "glyphs/DIN0115_Signaluebergabe.svg")
addIcon(regular,  119, "glyphs/DIN0119_Eingang.svg")
addIcon(regular,  120, "glyphs/DIN0120_Ausgang.svg")
addIcon(regular,  127, "glyphs/DIN0127_Ventilation_Lueftung.svg")
addIcon(regular,  129, "glyphs/DIN0129_Hinweispfeil.svg")
addIcon(regular,  131, "glyphs/DIN0131_Gefaehrliche_elektrische_Spannung.svg")
addIcon(regular,  132, "glyphs/DIN0132_Waermeabgabe_durch_Strahlung.svg")
addIcon(regular,  133, "glyphs/DIN0133_Waermeabgabe_durch_Konvektion.svg")
addIcon(regular,  139, "glyphs/DIN0139_Lampe_Licht_Beleuchtung.svg")
addIcon(regular,  153, "glyphs/DIN0153_Leuchtmelder_Signalleuchte.svg")
addIcon(regular,  164, "glyphs/DIN0164_Zaehlen.svg")
addIcon(regular,  165, "glyphs/DIN0165_Messen.svg")
addIcon(regular,  166, "glyphs/DIN0166_Pruefen.svg")
addIcon(regular,  167, "glyphs/DIN0167_Kupplung_allgemein.svg")
addIcon(regular,  168, "glyphs/DIN0168_Drehen_Umdrehung_Drehzahl_Gantrydrehung.svg")
addIcon(regular,  169, "glyphs/DIN0169_Gleichzeitige_Bewegung_in_entgegengesetzter_Richtung_aus_zwei_Begrenzungen_heraus.svg")
addIcon(regular,  170, "glyphs/DIN0170_Thermometer.svg")
addIcon(regular,  171, "glyphs/DIN0171_Temperaturabnahme.svg")
addIcon(regular,  172, "glyphs/DIN0172_Temperaturzunahme.svg")
addIcon(regular,  173, "glyphs/DIN0173_Uhr_Zeitschalter_Zeitgeber.svg")
addIcon(regular,  174, "glyphs/DIN0174_Getriebe_allgemein.svg")
addIcon(regular,  176, "glyphs/DIN0176_Drehbewegung_in_zwei_Richtungen.svg")
addIcon(regular,  200, "glyphs/DIN0200_Stoerung.svg")
addIcon(regular,  214, "glyphs/DIN0214_Bewegung_in_Pfeilrichtung_begrenzt.svg")
addIcon(regular,  217, "glyphs/DIN0217_Einmalige_Umdrehung.svg")
addIcon(regular,  253, "glyphs/DIN0253_Elektrischer_Hauptschalter.svg")
addIcon(regular,  254, "glyphs/DIN0254_Bewegung_hin_und_zurueck_in_Pfeilrichtung_begrenzt.svg")
addIcon(regular,  257, "glyphs/DIN0257_Ablassen_Ablassoeffnung.svg")
addIcon(regular,  258, "glyphs/DIN0258_Ueberlauf.svg")
addIcon(regular,  259, "glyphs/DIN0259_Gleichzeitige_Bewegung_aus_entgegengesetzter_Richtung_auf_eine_gemeinsame_Begrenzung_zu.svg")
addIcon(regular,  267, "glyphs/DIN0267_Automatischer_Ablauf.svg")
addIcon(regular,  268, "glyphs/DIN0268_Bewegung_in_Pfeilrichtung_unterbrochen.svg")
addIcon(regular,  269, "glyphs/DIN0269_Bewegung_in_zwei_Richtungen.svg")
addIcon(regular,  270, "glyphs/DIN0270_Wirkung_von_einem_Bezugspunkt_aus.svg")
addIcon(regular,  271, "glyphs/DIN0271_Wirkung_auf_einen_Bezugspunkt_zu.svg")
addIcon(regular,  272, "glyphs/DIN0272_Bewegung_in_Pfeilrichtung_aus_einer_Begrenzung.svg")
addIcon(regular,  273, "glyphs/DIN0273_Mechanische_Energie.svg")
addIcon(regular,  274, "glyphs/DIN0274_Pneumatische_Energie.svg")
addIcon(regular,  275, "glyphs/DIN0275_Waerme_Energie.svg")
addIcon(regular,  276, "glyphs/DIN0276_Dampf_Energie.svg")
addIcon(regular,  277, "glyphs/DIN0277_Wasser_Energie.svg")
addIcon(regular,  278, "glyphs/DIN0278_Elektrische_Energie.svg")
addIcon(regular,  279, "glyphs/DIN0279_Hydraulische_Energie.svg")
addIcon(regular,  282, "glyphs/DIN0282_Oszillierende_Bewegung_beidseitig_begrenzt.svg")
addIcon(regular,  305, "glyphs/DIN0305_Quittierung.svg")
addIcon(regular,  306, "glyphs/DIN0306_Einmalige_Verwendung.svg")
addIcon(regular,  308, "glyphs/DIN0308_Schriftzeichenabdruck_korrigieren_Rueckwaertsschritt_mit_Tilgen.svg")
addIcon(regular,  309, "glyphs/DIN0309_Aufwickeln.svg")
addIcon(regular,  310, "glyphs/DIN0310_Abwickeln.svg")
addIcon(regular,  315, "glyphs/DIN0315_Warenbahn_transportieren.svg")
addIcon(regular,  342, "glyphs/DIN0342_Buersten_mit_Rotationsbuerste.svg")
addIcon(regular,  345, "glyphs/DIN0345_Spruehen.svg")
addIcon(regular,  354, "glyphs/DIN0354_Sauberkeitsstufe_1.svg")
addIcon(regular,  355, "glyphs/DIN0355_Sauberkeitsstufe_2.svg")
addIcon(regular,  356, "glyphs/DIN0356_Sauberkeitsstufe_3.svg")
addIcon(regular,  366, "glyphs/DIN0366_Gleichphasige_Vorgaenge.svg")
addIcon(regular,  367, "glyphs/DIN0367_Ungleichphasige_Vorgaenge.svg")
addIcon(regular,  369, "glyphs/DIN0369_Tauchtiefe.svg")
addIcon(regular,  370, "glyphs/DIN0370_Oszillierende_Drehbewegung_beidseitig_begrenzt.svg")
addIcon(regular,  375, "glyphs/DIN0375_Trinkgefaess_fuellen_Becher_fuellen.svg")
addIcon(regular,  376, "glyphs/DIN0376_Spuelen_von_Behaeltnissen_Schalenspuelung.svg")
addIcon(regular,  403, "glyphs/DIN0403_Wasserdampf.svg")
addIcon(regular,  440, "glyphs/DIN0440_Behaeltnis.svg")
addIcon(regular,  441, "glyphs/DIN0441_Fuellstandsanzeige.svg")
addIcon(regular,  448, "glyphs/DIN0448_Umdrehung_je_Minute.svg")
addIcon(regular,  449, "glyphs/DIN0449_Verdampfer_Vakuumpumpe.svg")
addIcon(regular,  453, "glyphs/DIN0453_Wirkung_aus_zwei_Richtungen_auf_einen_Bezugspunkt_hin.svg")
addIcon(regular,  459, "glyphs/DIN0459_Bewegung_aus_einer_Begrenzung_in_Pfeilrichtung_Begrenzt.svg")
addIcon(regular,  461, "glyphs/DIN0461_Bewegung_in_zwei_Richtungen_begrenzt.svg")
addIcon(regular,  462, "glyphs/DIN0462_Datenspeicher.svg")
addIcon(regular,  474, "glyphs/DIN0474_Waermeabgabe_allgemein.svg")
addIcon(regular,  483, "glyphs/DIN0483_Wasser.svg")
addIcon(regular,  484, "glyphs/DIN0484_Reinigen_manuell.svg")
addIcon(regular,  485, "glyphs/DIN0485_Luft.svg")
addIcon(regular,  491, "glyphs/DIN0491_Kuehlen.svg")
addIcon(regular,  492, "glyphs/DIN0492_Abstreichen_Escape.svg")
addIcon(regular,  510, "glyphs/DIN0510_Rakler_Abstreifer.svg")
addIcon(regular,  519, "glyphs/DIN0519_Temperatur_regeln.svg")
addIcon(regular,  520, "glyphs/DIN0520_Niveau_regeln.svg")
addIcon(regular,  523, "glyphs/DIN0523_Nicht_im_Lauf_betaetigen.svg")
addIcon(regular,  524, "glyphs/DIN0524_Nur_im_Lauf_betaetigen.svg")
addIcon(regular,  562, "glyphs/DIN0562_Nullstellung.svg")
addIcon(regular,  582, "glyphs/DIN0582_Trichter.svg")
addIcon(regular,  627, "glyphs/DIN0627_Waermeverbraucher_allgemein.svg")
addIcon(regular,  635, "glyphs/DIN0635_Elektromotor_allgemein.svg")
addIcon(regular,  636, "glyphs/DIN0636_Stromerzeuger_umlaufend_allgemein.svg")
addIcon(regular,  637, "glyphs/DIN0637_Ventilator_allgemein.svg")
addIcon(regular,  638, "glyphs/DIN0638_Ventilator_radial.svg")
addIcon(regular,  639, "glyphs/DIN0639_Ventilator_axial.svg")
addIcon(regular,  681, "glyphs/DIN0681_Druckmessung.svg")
addIcon(regular,  682, "glyphs/DIN0682_Dehnung.svg")
addIcon(regular,  683, "glyphs/DIN0683_Dehnungsmessung.svg")
addIcon(regular,  684, "glyphs/DIN0684_Schwingungsmessung.svg")
addIcon(regular,  685, "glyphs/DIN0685_Drehzahlmessung.svg")
addIcon(regular,  686, "glyphs/DIN0686_Durchfluss.svg")
addIcon(regular,  687, "glyphs/DIN0687_Durchflussmessung.svg")
addIcon(regular,  688, "glyphs/DIN0688_Temperaturmessung.svg")
addIcon(regular,  691, "glyphs/DIN0691_Hoehenstand_Niveau.svg")
addIcon(regular,  695, "glyphs/DIN0695_Fluessigkeitspumpe_allgemein.svg")
addIcon(regular,  696, "glyphs/DIN0696_Verdraengerpumpe_oszillierend.svg")
addIcon(regular,  697, "glyphs/DIN0697_Hubkolbenpumpe.svg")
addIcon(regular,  698, "glyphs/DIN0698_Axialkolbenpumpe.svg")
addIcon(regular,  699, "glyphs/DIN0699_Radialkolbenpumpe.svg")
addIcon(regular,  700, "glyphs/DIN0700_Membranpumpe.svg")
addIcon(regular,  701, "glyphs/DIN0701_Verdraengerpumpe_rotierend.svg")
addIcon(regular,  704, "glyphs/DIN0704_Kreiskolbenpumpe.svg")
addIcon(regular,  708, "glyphs/DIN0708_Kreiselpumpe.svg")
addIcon(regular,  713, "glyphs/DIN0713_Kuehlmittelpumpe.svg")
addIcon(regular,  714, "glyphs/DIN0714_Wasserpumpe.svg")
addIcon(regular,  715, "glyphs/DIN0715_Verdichter_allgemein_Vakuumpumpe_allgemein.svg")
addIcon(regular,  776, "glyphs/DIN0776_Hoehenstandsmessung_Niveaumessung.svg")
addIcon(regular,  869, "glyphs/DIN0869_Walze_angelegt.svg")
addIcon(regular,  870, "glyphs/DIN0870_Walze_abgehoben.svg")
addIcon(regular,  873, "glyphs/DIN0873_Beimischen_Zumischen.svg")
addIcon(regular,  874, "glyphs/DIN0874_Temperaturwaechter.svg")
addIcon(regular,  875, "glyphs/DIN0875_Druckwaechter.svg")
addIcon(regular,  887, "glyphs/DIN0887_Walzen.svg")
addIcon(regular,  932, "glyphs/DIN0932_Frequenz_regeln.svg")
addIcon(regular,  988, "glyphs/DIN0988_Kuehlung_mit_Luft.svg")
addIcon(regular,  989, "glyphs/DIN0989_Kuehlung_mit_Wasser.svg")
addIcon(regular,  995, "glyphs/DIN0995_Angleichen_von_Geschwindigkeiten.svg")
addIcon(regular,  996, "glyphs/DIN0996_Druck_regeln.svg")
addIcon(regular,  997, "glyphs/DIN0997_Drehzahl_regeln.svg")
addIcon(regular, 1002, "glyphs/DIN1002_Endschalter_allgemein.svg")
addIcon(regular, 1003, "glyphs/DIN1003_Walzen_schließen_Walzen_zusammenfahren.svg")
addIcon(regular, 1004, "glyphs/DIN1004_Walzen_abheben_Walzen_auseinanderfahren.svg")
addIcon(regular, 1019, "glyphs/DIN1019_Linksdrehung_Linkslauf.svg")
addIcon(regular, 1024, "glyphs/DIN1024_Untere_Walze_anlegen.svg")
addIcon(regular, 1025, "glyphs/DIN1025_Obere_Walze_anlegen.svg")
addIcon(regular, 1040, "glyphs/DIN1040_Schwerkraftabscheider_allgemein.svg")
addIcon(regular, 1041, "glyphs/DIN1041_Schwerkraft_Gegenstromabscheider.svg")
addIcon(regular, 1042, "glyphs/DIN1042_Schwerkraft_Querstromabscheider.svg")
addIcon(regular, 1043, "glyphs/DIN1043_Schwerkraft_Umlenkabscheider.svg")
addIcon(regular, 1109, "glyphs/DIN1109_Vorbereitendes_Schalten_auf_eine_vorzuwaehlende_Drehzahl.svg")
addIcon(regular, 1110, "glyphs/DIN1110_Vorgewaehlte_Drehzahl_loeschen.svg")
addIcon(regular, 1111, "glyphs/DIN1111_Ingangsetzen_auf_vorgewaehlte_Drehzahl.svg")
addIcon(regular, 1118, "glyphs/DIN1118_Abstreifer_angestell_angelegt_Rakel_angestellt_angelegt.svg")
addIcon(regular, 1119, "glyphs/DIN1119_Abstreifer_abgestellt_abgehoben_Rakel_abgestellt_abgehoben.svg")
addIcon(regular, 1127, "glyphs/DIN1127_Behaelter_gefuellt.svg")
addIcon(regular, 1129, "glyphs/DIN1129_Behaelter_teilgefuellt.svg")
addIcon(regular, 1130, "glyphs/DIN1130_Behaelter_leer.svg")
addIcon(regular, 1153, "glyphs/DIN1153_Drehbewegung_in_Produktionsrichtung.svg")
addIcon(regular, 1154, "glyphs/DIN1154_Drehbewegung_entgegen_Produktionsrichtung.svg")
addIcon(regular, 1155, "glyphs/DIN1155_Unterbrochene_Drehbewegung_in_Produktionsrichtung.svg")
addIcon(regular, 1156, "glyphs/DIN1156_Unterbrochene_Drehbewegung_entgegen_Produktionsrichtung.svg")
addIcon(regular, 1222, "glyphs/DIN1222_Einlauf_in_die_Maschine.svg")
addIcon(regular, 1223, "glyphs/DIN1223_Auslauf_aus_der_Maschine.svg")
addIcon(regular, 1225, "glyphs/DIN1225_Walze_allgemein.svg")
addIcon(regular, 1226, "glyphs/DIN1226_Buerstwalze_abgehoben.svg")
addIcon(regular, 1254, "glyphs/DIN1254_Fuehler_allgemein_Messort_Waechter.svg")
addIcon(regular, 1261, "glyphs/DIN1261_Veraendern_einer_Warenbahnspannung_Fadenzug_mit_markierter_Ausgangsstellung.svg")
addIcon(regular, 1265, "glyphs/DIN1265_Drehzahl_aendern.svg")
addIcon(regular, 1279, "glyphs/DIN1279_Auge_Kontrollieren_Pruefen.svg")
addIcon(regular, 1287, "glyphs/DIN1287E_Fluessig_sichern_Kleben_Dichten.svg")
addIcon(regular, 1293, "glyphs/DIN1293_Einoelen_Oel.svg")
addIcon(regular, 1384, "glyphs/DIN1384_Stand_zu_niedring.svg")
addIcon(regular, 1385, "glyphs/DIN1385_Stand_zu_hoch.svg")
addIcon(regular, 1416, "glyphs/DIN1416_Bewegung_rechtsdrehend_aus_einer_Begrenzung.svg")
addIcon(regular, 1418, "glyphs/DIN1418_Druckluftschaltung.svg")
addIcon(regular, 1420, "glyphs/DIN1420_Bewegung_linksdrehend_aus_einer_Begrenzung.svg")
addIcon(regular, 1429, "glyphs/DIN1429_Schaummittel.svg")
addIcon(regular, 1431, "glyphs/DIN1431_Netzmittel.svg")
addIcon(regular, 1480, "glyphs/DIN1480_Temperatur_zu_hoch.svg")
addIcon(regular, 1481, "glyphs/DIN1481_Temperatur_zu_niedrig.svg")
addIcon(regular, 1699, "glyphs/DIN1699_Nullpunktverschiebung.svg")
addIcon(regular, 1758, "glyphs/DIN1758_Veraendern_einer_Groesse_in_Stufen.svg")
addIcon(regular, 1781, "glyphs/DIN1781_Messwertaufnehmer.svg")
addIcon(regular, 1849, "glyphs/DIN1849_Start_tastend.svg")
addIcon(regular, 1900, "glyphs/DIN1900_Orientierter_Stop.svg")

addIcon(regular, 2051, "glyphs/DIN2051_Behaelterinhalt_austauschen.svg")

addIcon(regular, 2146, "glyphs/DIN2146_Drehrichtung_im_Uhrzeigersinn.svg")
addIcon(regular, 2159, "glyphs/DIN2159_Drehrichtung_entgegen_Uhrzeigersinn.svg")
addIcon(regular, 2187, "glyphs/DIN2187_Positionieren.svg")
addIcon(regular, 2200, "glyphs/DIN2200_Reinigung_automatisch.svg")
addIcon(regular, 2201, "glyphs/DIN2201_Nicht_betaetigen_nicht_eingreifen.svg")

addIcon(regular, 2301, "glyphs/DIN2301_Programm_ohne_Maschinen_Funktionen.svg")
addIcon(regular, 2302, "glyphs/DIN2302_Programm_mit_Maschinen_Funktionen.svg")
addIcon(regular, 2303, "glyphs/DIN2303_Bezugspunkt.svg")
addIcon(regular, 2306, "glyphs/DIN2306_Veraendern.svg")
addIcon(regular, 2307, "glyphs/DIN2307_Programm_einlesen_ohne_Maschinen_Funktionen.svg")
addIcon(regular, 2308, "glyphs/DIN2308_Programm_einlesen_mit_Maschinen_Funktionen.svg")
addIcon(regular, 2309, "glyphs/DIN2309_Satzweises_Einlesen_ohne_Maschinen_Funktionen.svg")
addIcon(regular, 2310, "glyphs/DIN2310_Satzweises_Einlesen_mit_Maschinen_Funktionen.svg")
addIcon(regular, 2311, "glyphs/DIN2311_Programm_veraendern.svg")
addIcon(regular, 2312, "glyphs/DIN2312_Unterprogramm.svg")

addIcon(regular, 2315, "glyphs/DIN2315_Suchlauf_vorwaerts.svg")
addIcon(regular, 2316, "glyphs/DIN2316_Suchlauf_rueckwaerts.svg")
addIcon(regular, 2317, "glyphs/DIN2317_Satznummern_Suche_vorwaerts.svg")
addIcon(regular, 2318, "glyphs/DIN2318_Satznummern_Suche_rueckwaerts.svg")
addIcon(regular, 2319, "glyphs/DIN2319_Hauptsatz_Suche_vorwaerts.svg")
addIcon(regular, 2320, "glyphs/DIN2320_Hauptsatz_Suche_rueckwaerts.svg")
addIcon(regular, 2321, "glyphs/DIN2321_Satz_Unterdrueckung.svg")
addIcon(regular, 2322, "glyphs/DIN2322_Programm_Anfang.svg")
addIcon(regular, 2323, "glyphs/DIN2323_Programm_Ende.svg")
addIcon(regular, 2324, "glyphs/DIN2324_Programm_Ende_mit_Lochstreifen_Ruecklauf_bis_Programm_Anfang.svg")
addIcon(regular, 2325, "glyphs/DIN2325_Suchlauf_rueckwaerts_zum_Programm_Anfang.svg")
addIcon(regular, 2326, "glyphs/DIN2326_Programmierter_Halt.svg")
addIcon(regular, 2327, "glyphs/DIN2327_Wahlweiser_programmierter_Halt.svg")

addIcon(regular, 2330, "glyphs/DIN2330_Handeingabe.svg")

addIcon(regular, 2335, "glyphs/DIN2335_Absolute_Massangabe.svg")
addIcon(regular, 2336, "glyphs/DIN2336_Relative_Massangabe.svg")
addIcon(regular, 2337, "glyphs/DIN2337_Referenzpunkt.svg")
addIcon(regular, 2338, "glyphs/DIN2338_Gitterpunkt.svg")
addIcon(regular, 2339, "glyphs/DIN2339_Koordinaten_Nullpunkt.svg")

addIcon(regular, 2341, "glyphs/DIN2341_Senden_aus_Speicher.svg")
addIcon(regular, 2342, "glyphs/DIN2342_Empfangen_in_Speicher.svg")
addIcon(regular, 2345, "glyphs/DIN2345_Nullpunkt_Korrektur.svg")
addIcon(regular, 2346, "glyphs/DIN2346_Positioniergenaugikeit_fein.svg")
addIcon(regular, 2347, "glyphs/DIN2347_Positioniergenaugikeit_mittel.svg")
addIcon(regular, 2348, "glyphs/DIN2348_Positioniergenauigkeit_grob.svg")
addIcon(regular, 2349, "glyphs/DIN2349_Datenaufzeichnung_in_einen_Speicher_Enter_Datenfreigabe.svg")
addIcon(regular, 2350, "glyphs/DIN2350_Daten_lesen_aus_einem_Speicher.svg")

addIcon(regular, 2362, "glyphs/DIN2362_Position.svg")
addIcon(regular, 2367, "glyphs/DIN2367_Bereit_fertig.svg")
addIcon(regular, 2371, "glyphs/DIN2371_Nicht_bereit.svg")
addIcon(regular, 2373, "glyphs/DIN2373_Testlauf.svg")
addIcon(regular, 2391, "glyphs/DIN2391_Programmmierbarer_Zeitgeber.svg")

addIcon(regular, 2401, "glyphs/DIN2401E_Verpackung_offen_leer_Papierbehaelter_leer_verfuegbar.svg")
addIcon(regular, 2402, "glyphs/DIN2402E_Verpackung_geschlossen_leer.svg")
addIcon(regular, 2403, "glyphs/DIN2403E_Kein_Packmittel.svg")
addIcon(regular, 2404, "glyphs/DIN2404E_Verpackung_offen_gefuellt.svg")
addIcon(regular, 2405, "glyphs/DIN2405E_Verpackung_geschlossen_gefuellt.svg")
addIcon(regular, 2406, "glyphs/DIN2406E_Deckel_Verschluss.svg")
addIcon(regular, 2407, "glyphs/DIN2407E_Deckel_fehlt_Verschluss_fehlt.svg")
addIcon(regular, 2409, "glyphs/DIN2409E_Becher_Behaeltnis.svg")
addIcon(regular, 2410, "glyphs/DIN2410E_Kein_Becher_Kein_Behaeltnis.svg")
addIcon(regular, 2411, "glyphs/DIN2411E_Becher_Behaeltnis_Verschluss.svg")
addIcon(regular, 2412, "glyphs/DIN2412E_Bescherverschluss_anheften.svg")


addIcon(regular, 2434, "glyphs/DIN2434E_Fluessig.svg")
addIcon(regular, 2439, "glyphs/DIN2439_Fuellhoehe_messen_Fuellstandskontrolle.svg")
addIcon(regular, 2440, "glyphs/DIN2440_Fuellhoehe_veraendern_Fuellmenge_veraendern.svg")
addIcon(regular, 2449, "glyphs/DIN2449_Durchflußregelung.svg")
addIcon(regular, 2450, "glyphs/DIN2450_Wasserbehaelter_Wasserbecken.svg")
addIcon(regular, 2451, "glyphs/DIN2451_Wassertemperatur.svg")
addIcon(regular, 2453, "glyphs/DIN2453_Heizung_geregelt.svg")
addIcon(regular, 2586, "glyphs/DIN2586_Druck_zu_hoch.svg")
addIcon(regular, 2587, "glyphs/DIN2587_Druck_zu_niedring.svg")
addIcon(regular, 2603, "glyphs/DIN2603_Wasserdruck.svg")
addIcon(regular, 2679, "glyphs/DIN2679_Stoff_Fluss_entgegen_Produktionsrichtung.svg")
addIcon(regular, 2680, "glyphs/DIN2680_Stoff_Fluss_in_Produktionsrichtung.svg")
addIcon(regular, 2692, "glyphs/DIN2692_Geschwindigkeitsregelung_m_min.svg")
addIcon(regular, 2693, "glyphs/DIN2693_Vorbereitendes_Schalten_einer_Zeitspanne_in_Minuten.svg")
addIcon(regular, 2757, "glyphs/DIN2757_Filter_verschmutzt.svg")
addIcon(regular, 2913, "glyphs/DIN2913_Wasserzulauf.svg")

addIcon(regular, 2959, "glyphs/DIN2959_Kundendienst_rufen.svg")
addIcon(regular, 2960, "glyphs/DIN2960_Toner_trocken_nachfuellen.svg")
addIcon(regular, 2961, "glyphs/DIN2961_Farbe_nachfuellen.svg")
addIcon(regular, 2962, "glyphs/DIN2962_Toner_fluessig_nachfuellen.svg")
addIcon(regular, 2963, "glyphs/DIN2963_Dispersant_nachfuellen.svg")
addIcon(regular, 2964, "glyphs/DIN2964_Entwickler_nachfuellen_gebrauchsfertig.svg")
addIcon(regular, 2965, "glyphs/DIN2965_Wasser_nachfuellen.svg")

addIcon(regular, 2993, "glyphs/DIN2993_Recovery_Recycling_allgemein.svg")
addIcon(regular, 3103, "glyphs/DIN3103_Rotationsbuerste.svg")
addIcon(regular, 3271, "glyphs/DIN3271_Ruecksetzen_in_den_Ausgangszustand.svg")
addIcon(regular, 3328, "glyphs/DIN3328_Elektronische_Berechtigung.svg")
addIcon(regular, 3330, "glyphs/DIN3330_Information.svg")
addIcon(regular, 3559, "glyphs/DIN3559_Wasserzulauf_offen.svg")
addIcon(regular, 3663, "glyphs/DIN3663_Waermestrahlung_von_Warenbahn_abgewendet.svg")
addIcon(regular, 3664, "glyphs/DIN3664_Waermestrahlung_auf_Warenbahn_gerichtet.svg")
addIcon(regular, 3677, "glyphs/DIN3677_Geschwindigkeitsdifferenz_in_Prozent.svg")
addIcon(regular, 3678, "glyphs/DIN3678_Geschwindigkeitsdifferenz_hundert_Prozent.svg")
addIcon(regular, 3764, "glyphs/DIN3764_Ausschaltzeit.svg")
addIcon(regular, 3765, "glyphs/DIN3765_Einschaltzeit.svg")
addIcon(regular, 3766, "glyphs/DIN3766_Betriebsdauer.svg")
addIcon(regular, 3813, "glyphs/DIN3813_Anzeige_der_verbleibenden_Zeit.svg")
addIcon(regular, 3814, "glyphs/DIN3814_Anzeige_der_abgelaufenen_Zeit.svg")
addIcon(regular, 3846, "glyphs/DIN3846_NotAus.svg")
addIcon(regular, 3882, "glyphs/DIN3882_Vorherige_Seite.svg")
addIcon(regular, 3883, "glyphs/DIN3883_Naechste_Seite.svg")
addIcon(regular, 3903, "glyphs/DIN3903_Eingang_Ausgang.svg")







# export to files
flags = ("opentype", "dummy-dsig", "round", "apple")

regular.generate ("out/DIN_30600.ttf", flags=flags)
regular.close()

#bold.generate ("out/NIPAJIN-Dingbats-Bold.ttf", flags=flags)
#bold.close()

#italic.generate ("out/NIPAJIN-Dingbats-Italic.ttf", flags=flags)
#italic.close()
