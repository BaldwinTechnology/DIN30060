#!/usr/bin/python
# -*- coding: utf-8 -*-
# simple .svg to .ttf icon font converter, (c) 2020–2021 Baldi

# generate.py file taken from nipajin-dingbats

import fontforge, psMat

fontname = "DIN30600"
fullname = "DIN 30600 graphical symbols"
familyname = "DIN 30600"
version = "v1.1"
copyright = "Copyright (c) 2020–2021, Baldi, Reserved Font Name \"DIN 30600\".\n\nThis Font Software is licensed under the SIL Open Font License, Version 1.1.\nThis license is available with a FAQ at: http://scripts.sil.org/OFL"

def addIcon( font, glyph, svgFileName, name="" ):
    "add a svg as icon glyph"
    glyph = font.createChar(glyph)
    glyph.importOutlines(svgFileName)

    if name == '':
        # "glyphs/DIN0003_Lesen_oder_Wiedergabe_von_einem_Informationstraeger.svg
        #  1...5...10....5...20
        text = svgFileName[:-4] # remove '.svg'
        text = text[15:] # remove the first 15 characters
        text = text.replace("_", " ")

        name = text
        #print (name)
    glyph.glyphname = name
    glyph.comment = name

    glyph.correctDirection()
    return;

# start with a new font
regular = fontforge.font()  # shape only

# add some meta-data
regular.fontname = fontname + "-Regular"
regular.fullname = fullname
regular.familyname = familyname
regular.version = version
regular.copyright = copyright


# add symbols
# addIcon   (regular, ord('4'), "glyphs/d10.svg") // example

#Page 07
addIcon(regular,    3, "glyphs/DIN0003_Lesen_oder_Wiedergabe_von_einem_Informationstraeger.svg", "Lesen oder Wiedergabe von einem Informationsträger")
addIcon(regular,    4, "glyphs/DIN0004_Loeschen_einer_Information_von_einem_Informationstraeger.svg")
addIcon(regular,    9, "glyphs/DIN0009_Steuern.svg")
addIcon(regular,   10, "glyphs/DIN0010_Regeln.svg")
addIcon(regular,   11, "glyphs/DIN0011_Start_eines_Vorganges.svg", "Start (eines Vorganges")
addIcon(regular,   12, "glyphs/DIN0012_Schnellstart.svg")
addIcon(regular,   13, "glyphs/DIN0013_Stop_eines_Vorganges_Abbrechen.svg", "Stop (eines Vorganges); Abbrechen")
addIcon(regular,   14, "glyphs/DIN0014_Schnellstop.svg")
addIcon(regular,   15, "glyphs/DIN0015_Aus_Ausschalten_oder_Ausgeschaltet.svg", "Aus (Ausschalten oder Ausgeschaltet)")
addIcon(regular,   16, "glyphs/DIN0016_Ein_Einschalten_oder_Eingeschaltet.svg", "Ein (Einschalten oder Eingeschaltet)")
addIcon(regular,   17, "glyphs/DIN0017_Bereit.svg", "Bereitschaftsstellung")
addIcon(regular,   18, "glyphs/DIN0018_Ein_Aus_Drucktaste_mit_zwei_festen_Stellungen.svg", "Ein/Aus-Drucktaste mit zwei festen Stellungen")
addIcon(regular,   19, "glyphs/DIN0019_Ein_Aus_Drucktaster.svg", "Ein/Aus (Drucktaster)")
addIcon(regular,   20, "glyphs/DIN0020_Abschalten.svg")
addIcon(regular,   21, "glyphs/DIN0021_Zuschalten.svg")
addIcon(regular,   22, "glyphs/DIN0022_Bereitschaftsstellung_fuer_einen_Teil_des_Betriebsmittels.svg")
addIcon(regular,   23, "glyphs/DIN0023_Veraendern_einer_Groesse.svg", "Verändern einer Größe")
addIcon(regular,   24, "glyphs/DIN0024_Maximaleinstellung.svg")
addIcon(regular,   25, "glyphs/DIN0025_Minimumeinstellung.svg")
addIcon(regular,   26, "glyphs/DIN0026_Eichen_Kalibrieren.svg", "Eichen; Kalibrieren")
addIcon(regular,   27, "glyphs/DIN0027_Aufnahme_auf_einen_Informationstraeger.svg", "Aufnahme auf einen Informationsträger")
addIcon(regular,   28, "glyphs/DIN0028_Bewegung_in_eine_Richtung.svg")
addIcon(regular,   29, "glyphs/DIN0029_Rueckuebertragung.svg", "Rückübertragung")
addIcon(regular,   30, "glyphs/DIN0030_Nichtrechnen.svg")
addIcon(regular,   31, "glyphs/DIN0031_Zwischenresultat.svg")
addIcon(regular,   32, "glyphs/DIN0032_Resultat.svg")
addIcon(regular,   35, "glyphs/DIN0035_Handbetaetigung.svg", "Handbetätigung")
addIcon(regular,   42, "glyphs/DIN0042_Elektrische_Maschine.svg")
addIcon(regular,   45, "glyphs/DIN0045_Entriegeln.svg")
addIcon(regular,   46, "glyphs/DIN0046_Verriegeln.svg")
addIcon(regular,   47, "glyphs/DIN0047_Zentrale_Schaltstelle.svg")
addIcon(regular,   56, "glyphs/DIN0056_Mittelstellung.svg")
addIcon(regular,   80, "glyphs/DIN0080_Zulaessige_Uebertemperatur.svg", "Zulässige Übertemperatur")
addIcon(regular,   82, "glyphs/DIN0082_Maschineninterne_Uebertragung_von_Daten.svg", "Maschineninterne Übertragung von Daten")
addIcon(regular,   84, "glyphs/DIN0084_Konstanten_Eingabe.svg", "Konstanten-Eingabe")
addIcon(regular,   85, "glyphs/DIN0085_Konstanten_Abruf.svg", "Konstanten-Abruf")
addIcon(regular,   86, "glyphs/DIN0086_Gesamtloeschen_Gesamt_Nullstellen.svg", "Gesamtlöschen; gesamt-Nullstellen")
addIcon(regular,   88, "glyphs/DIN0088_Maschinelles_Runden.svg")
addIcon(regular,   89, "glyphs/DIN0089_Schnelle_Bewegung_in_eine_Begrenzung.svg")
addIcon(regular,   90, "glyphs/DIN0090_Schnelle_Bewegung_aus_einer_Begrenzung.svg")
addIcon(regular,  100, "glyphs/DIN0100_Drehbewegung_nach_rechts.svg")
#Page 09
addIcon(regular,  101, "glyphs/DIN0101_Entfernungsringe.svg")
addIcon(regular,  102, "glyphs/DIN0102_Peilzeigereinstellung.svg")
addIcon(regular,  105, "glyphs/DIN0105_Taster_handbetaetigt.svg", "Taster, handbetätigt")
addIcon(regular,  111, "glyphs/DIN0111_Impulsmarkierung_auf_Informationstraeger.svg", "Impulsmarkierung auf Informationsträger")
addIcon(regular,  112, "glyphs/DIN0112_Trennschnitt.svg")
addIcon(regular,  113, "glyphs/DIN0113_Pause_Unterbrechung.svg", "Pause; Unterbrechung")
addIcon(regular,  114, "glyphs/DIN0114_Drehbewegung_nach_links.svg")
addIcon(regular,  115, "glyphs/DIN0115_Signaluebergabe.svg", "Signalübergabe")
addIcon(regular,  119, "glyphs/DIN0119_Eingang.svg", "Eingang (für Energie und Signale)")
addIcon(regular,  120, "glyphs/DIN0120_Ausgang.svg", "Ausgang (für Energie und Signale)")
addIcon(regular,  127, "glyphs/DIN0127_Ventilation_Lueftung.svg", "Ventilation; Lüftung")
addIcon(regular,  129, "glyphs/DIN0129_Hinweispfeil.svg")
addIcon(regular,  131, "glyphs/DIN0131_Gefaehrliche_elektrische_Spannung.svg", "Gefährliche elektrische Spannung")
addIcon(regular,  132, "glyphs/DIN0132_Waermeabgabe_durch_Strahlung.svg", "Wärmeabgabe durch Strahlung")
addIcon(regular,  133, "glyphs/DIN0133_Waermeabgabe_durch_Konvektion.svg", "Wärmeabgabe duch Konvektion")
addIcon(regular,  139, "glyphs/DIN0139_Lampe_Licht_Beleuchtung.svg", "Lampe; Licht; Beleuchtung")
addIcon(regular,  153, "glyphs/DIN0153_Leuchtmelder_Signalleuchte.svg", "Leuchtmelder; Signalleuchte")
addIcon(regular,  164, "glyphs/DIN0164_Zaehlen.svg", "Zählen")
addIcon(regular,  165, "glyphs/DIN0165_Messen.svg")
addIcon(regular,  166, "glyphs/DIN0166_Pruefen.svg", "Prüfen")
addIcon(regular,  167, "glyphs/DIN0167_Kupplung_allgemein.svg", "Kupplung, allgemein")
addIcon(regular,  168, "glyphs/DIN0168_Drehen_Umdrehung_Drehzahl_Gantrydrehung.svg", "Drehen; Umdrehung; Drehzahl; Gantrydrehung")
addIcon(regular,  169, "glyphs/DIN0169_Gleichzeitige_Bewegung_in_entgegengesetzter_Richtung_aus_zwei_Begrenzungen_heraus.svg")
addIcon(regular,  170, "glyphs/DIN0170_Thermometer.svg")
addIcon(regular,  171, "glyphs/DIN0171_Temperaturabnahme.svg")
addIcon(regular,  172, "glyphs/DIN0172_Temperaturzunahme.svg")
addIcon(regular,  173, "glyphs/DIN0173_Uhr_Zeitschalter_Zeitgeber.svg", "Uhr; Zeitschalter; Zeitgeber")
addIcon(regular,  174, "glyphs/DIN0174_Getriebe_allgemein.svg", "Getriebe, allgemein")
addIcon(regular,  176, "glyphs/DIN0176_Drehbewegung_in_zwei_Richtungen.svg")
addIcon(regular,  197, "glyphs/DIN0197_Temperatur_Begrenzer.svg", "Temperatur-Begrenzer")
addIcon(regular,  200, "glyphs/DIN0200_Stoerung.svg", "Störung")
#Page 11
addIcon(regular,  201, "glyphs/DIN0201_Begrenzer.svg")
addIcon(regular,  214, "glyphs/DIN0214_Bewegung_in_Pfeilrichtung_begrenzt.svg", "Bewegung in Pfeilrichtung, begrenzt")
addIcon(regular,  217, "glyphs/DIN0217_Einmalige_Umdrehung.svg")
addIcon(regular,  253, "glyphs/DIN0253_Elektrischer_Hauptschalter.svg")
addIcon(regular,  254, "glyphs/DIN0254_Bewegung_hin_und_zurueck_in_Pfeilrichtung_begrenzt.svg", "Bewegung hin und zurueck in Pfeilrichtung, begrenzt")
addIcon(regular,  256, "glyphs/DIN0256_Einfuellen_Einfuelloeffnung.svg", "Einfüllen; Einfüllöffnung")
addIcon(regular,  257, "glyphs/DIN0257_Ablassen_Ablassoeffnung.svg", "Ablassen; Ablaßöffnung")
addIcon(regular,  258, "glyphs/DIN0258_Ueberlauf.svg", "Überlauf")
addIcon(regular,  259, "glyphs/DIN0259_Gleichzeitige_Bewegung_aus_entgegengesetzter_Richtung_auf_eine_gemeinsame_Begrenzung_zu.svg")
addIcon(regular,  263, "glyphs/DIN0263_Blasen.svg")
addIcon(regular,  267, "glyphs/DIN0267_Automatischer_Ablauf.svg")
addIcon(regular,  268, "glyphs/DIN0268_Bewegung_in_Pfeilrichtung_unterbrochen.svg")
addIcon(regular,  269, "glyphs/DIN0269_Bewegung_in_zwei_Richtungen.svg")
addIcon(regular,  270, "glyphs/DIN0270_Wirkung_von_einem_Bezugspunkt_aus.svg")
addIcon(regular,  271, "glyphs/DIN0271_Wirkung_auf_einen_Bezugspunkt_zu.svg")
addIcon(regular,  272, "glyphs/DIN0272_Bewegung_in_Pfeilrichtung_aus_einer_Begrenzung.svg")
addIcon(regular,  273, "glyphs/DIN0273_Mechanische_Energie.svg")
addIcon(regular,  274, "glyphs/DIN0274_Pneumatische_Energie.svg")
addIcon(regular,  275, "glyphs/DIN0275_Waerme_Energie.svg", "Wärme-Energie")
addIcon(regular,  276, "glyphs/DIN0276_Dampf_Energie.svg", "Dampf-Energie")
addIcon(regular,  277, "glyphs/DIN0277_Wasser_Energie.svg", "Wasser-Energie")
addIcon(regular,  278, "glyphs/DIN0278_Elektrische_Energie.svg")
addIcon(regular,  279, "glyphs/DIN0279_Hydraulische_Energie.svg")
addIcon(regular,  282, "glyphs/DIN0282_Oszillierende_Bewegung_beidseitig_begrenzt.svg", "Oszillierende Bewegung, beidseitig begrenzt")
addIcon(regular,  299, "glyphs/DIN0299_Normallauf.svg")
addIcon(regular,  300, "glyphs/DIN0300_Schnellauf.svg")
#Page 13
addIcon(regular,  305, "glyphs/DIN0305_Quittierung.svg")
addIcon(regular,  306, "glyphs/DIN0306_Einmalige_Verwendung.svg")
addIcon(regular,  308, "glyphs/DIN0308_Schriftzeichenabdruck_korrigieren_Rueckwaertsschritt_mit_Tilgen.svg", "Schriftzeichenabdruck korrigieren; Rückwärtsschritt mit Tilgen")
addIcon(regular,  309, "glyphs/DIN0309_Aufwickeln.svg")
addIcon(regular,  310, "glyphs/DIN0310_Abwickeln.svg")
addIcon(regular,  315, "glyphs/DIN0315_Warenbahn_transportieren.svg")
addIcon(regular,  342, "glyphs/DIN0342_Buersten_mit_Rotationsbuerste.svg", "Bürsten mit Rotationsbürste")
addIcon(regular,  345, "glyphs/DIN0345_Spruehen.svg", "Sprühen")
addIcon(regular,  354, "glyphs/DIN0354_Sauberkeitsstufe_1.svg")
addIcon(regular,  355, "glyphs/DIN0355_Sauberkeitsstufe_2.svg")
addIcon(regular,  356, "glyphs/DIN0356_Sauberkeitsstufe_3.svg")
addIcon(regular,  366, "glyphs/DIN0366_Gleichphasige_Vorgaenge.svg", "Gleichphasige Vorgänge")
addIcon(regular,  367, "glyphs/DIN0367_Ungleichphasige_Vorgaenge.svg", "Ungleichphasige Vorgänge")
addIcon(regular,  369, "glyphs/DIN0369_Tauchtiefe.svg")
addIcon(regular,  370, "glyphs/DIN0370_Oszillierende_Drehbewegung_beidseitig_begrenzt.svg", "Oszillierende Drehbewegung, beidseitig begrenzt")
addIcon(regular,  375, "glyphs/DIN0375_Trinkgefaess_fuellen_Becher_fuellen.svg", "Trinkkgefäß füllen; Becherfüller")
addIcon(regular,  376, "glyphs/DIN0376_Spuelen_von_Behaeltnissen_Schalenspuelung.svg", "Spülen von Behältnissen; Schalenspülung")
#Page 15
addIcon(regular,  403, "glyphs/DIN0403_Wasserdampf.svg")
addIcon(regular,  440, "glyphs/DIN0440_Behaeltnis.svg", "Behältnis")
addIcon(regular,  441, "glyphs/DIN0441_Fuellstandsanzeige.svg", "Füllstandsanzeige")
addIcon(regular,  448, "glyphs/DIN0448_Umdrehung_je_Minute.svg")
addIcon(regular,  449, "glyphs/DIN0449_Verdampfer_Vakuumpumpe.svg", "Verdampfer-Vakuumpumpe")
addIcon(regular,  453, "glyphs/DIN0453_Wirkung_aus_zwei_Richtungen_auf_einen_Bezugspunkt_hin.svg")
addIcon(regular,  459, "glyphs/DIN0459_Bewegung_aus_einer_Begrenzung_in_Pfeilrichtung_Begrenzt.svg")
addIcon(regular,  461, "glyphs/DIN0461_Bewegung_in_zwei_Richtungen_begrenzt.svg", "Bewegung in zwei Richtungen, begrenzt")
addIcon(regular,  462, "glyphs/DIN0462_Datenspeicher.svg")
addIcon(regular,  472, "glyphs/DIN0472_Temperatur_Hoechstwertbegrenzung.svg", "Temperatur-Höchstwertbegrenzung")
addIcon(regular,  473, "glyphs/DIN0473_Temperatur_Tiefstwertbegrenzung.svg", "Temperatur-Tiefstwertbegrenzung")
addIcon(regular,  474, "glyphs/DIN0474_Waermeabgabe_allgemein.svg", "Wärmeabgabe, allgemein")
addIcon(regular,  480, "glyphs/DIN0480_Bewegung_vorwaerts.svg", "Bewegung vorwärts")
addIcon(regular,  481, "glyphs/DIN0481_Bewegung_rueckwaerts.svg", "Bewegung rückwärts")
addIcon(regular,  483, "glyphs/DIN0483_Wasser.svg")
addIcon(regular,  484, "glyphs/DIN0484_Reinigen_manuell.svg", "reinigen, manuell")
addIcon(regular,  485, "glyphs/DIN0485_Luft.svg")
addIcon(regular,  491, "glyphs/DIN0491_Kuehlen.svg", "Kühlen")
addIcon(regular,  492, "glyphs/DIN0492_Abstreichen_Escape.svg", "Abstreichen; Escape")
#Page 17
addIcon(regular,  510, "glyphs/DIN0510_Rakler_Abstreifer.svg")
addIcon(regular,  518, "glyphs/DIN0518_Feuchte_Wassergehalt.svg", "Feuchte; Wassergehalt")
addIcon(regular,  519, "glyphs/DIN0519_Temperatur_regeln.svg")
addIcon(regular,  520, "glyphs/DIN0520_Niveau_regeln.svg")
addIcon(regular,  523, "glyphs/DIN0523_Nicht_im_Lauf_betaetigen.svg")
addIcon(regular,  524, "glyphs/DIN0524_Nur_im_Lauf_betaetigen.svg")
addIcon(regular,  562, "glyphs/DIN0562_Nullstellung.svg")
addIcon(regular,  582, "glyphs/DIN0582_Trichter.svg")
#Page 19
addIcon(regular,  627, "glyphs/DIN0627_Waermeverbraucher_allgemein.svg", "Wärmeabgabe, allgemein")
addIcon(regular,  628, "glyphs/DIN0628_Becken_allgemein.svg", "Becken, allgemein")
addIcon(regular,  635, "glyphs/DIN0635_Elektromotor_allgemein.svg", "Elektromotor, allgemein")
addIcon(regular,  636, "glyphs/DIN0636_Stromerzeuger_umlaufend_allgemein.svg", "Stromerzeuger umlaufend, allgemein")
addIcon(regular,  637, "glyphs/DIN0637_Ventilator_allgemein.svg", "Ventilator, allgemein")
addIcon(regular,  638, "glyphs/DIN0638_Ventilator_radial.svg", "Ventilator, radial")
addIcon(regular,  639, "glyphs/DIN0639_Ventilator_axial.svg", "Ventialtor, axial")
addIcon(regular,  681, "glyphs/DIN0681_Druckmessung.svg")
addIcon(regular,  682, "glyphs/DIN0682_Dehnung.svg")
addIcon(regular,  683, "glyphs/DIN0683_Dehnungsmessung.svg")
addIcon(regular,  684, "glyphs/DIN0684_Schwingungsmessung.svg")
addIcon(regular,  685, "glyphs/DIN0685_Drehzahlmessung.svg")
addIcon(regular,  686, "glyphs/DIN0686_Durchfluss.svg", "Durchfluß")
addIcon(regular,  687, "glyphs/DIN0687_Durchflussmessung.svg")
addIcon(regular,  688, "glyphs/DIN0688_Temperaturmessung.svg")
addIcon(regular,  691, "glyphs/DIN0691_Hoehenstand_Niveau.svg", "Höhenstand, Niveau")
addIcon(regular,  695, "glyphs/DIN0695_Fluessigkeitspumpe_allgemein.svg", "Flüssigkeitspumpe, allgemein")
addIcon(regular,  696, "glyphs/DIN0696_Verdraengerpumpe_oszillierend.svg", "Verdrängerpumpe, oszillierend")
addIcon(regular,  697, "glyphs/DIN0697_Hubkolbenpumpe.svg")
addIcon(regular,  698, "glyphs/DIN0698_Axialkolbenpumpe.svg")
addIcon(regular,  699, "glyphs/DIN0699_Radialkolbenpumpe.svg")
addIcon(regular,  700, "glyphs/DIN0700_Membranpumpe.svg")
#Page 21
addIcon(regular,  701, "glyphs/DIN0701_Verdraengerpumpe_rotierend.svg", "Verdrängerpumpe, rotierend")
addIcon(regular,  704, "glyphs/DIN0704_Kreiskolbenpumpe.svg")
addIcon(regular,  708, "glyphs/DIN0708_Kreiselpumpe.svg")
addIcon(regular,  713, "glyphs/DIN0713_Kuehlmittelpumpe.svg", "Kühlmittelpumpe")
addIcon(regular,  714, "glyphs/DIN0714_Wasserpumpe.svg")
addIcon(regular,  715, "glyphs/DIN0715_Verdichter_allgemein_Vakuumpumpe_allgemein.svg", "Verdichter, allgemein; Vakuumpumpe, allgemein")
addIcon(regular,  776, "glyphs/DIN0776_Hoehenstandsmessung_Niveaumessung.svg", "Höhenstandsmessung; Niveaumessung")
#Page 23
addIcon(regular,  869, "glyphs/DIN0869_Walze_angelegt.svg")
addIcon(regular,  870, "glyphs/DIN0870_Walze_abgehoben.svg")
addIcon(regular,  873, "glyphs/DIN0873_Beimischen_Zumischen.svg", "Beimischen; Zumischen")
addIcon(regular,  874, "glyphs/DIN0874_Temperaturwaechter.svg", "Temperaturwächter")
addIcon(regular,  875, "glyphs/DIN0875_Druckwaechter.svg", "Druckwächter")
addIcon(regular,  887, "glyphs/DIN0887_Walzen.svg")
#Page 25
addIcon(regular,  932, "glyphs/DIN0932_Frequenz_regeln.svg")
addIcon(regular,  988, "glyphs/DIN0988_Kuehlung_mit_Luft.svg", "Kühlung mit Luft")
addIcon(regular,  989, "glyphs/DIN0989_Kuehlung_mit_Wasser.svg", "Kühlung mit Wasser")
addIcon(regular,  995, "glyphs/DIN0995_Angleichen_von_Geschwindigkeiten.svg")
addIcon(regular,  996, "glyphs/DIN0996_Druck_regeln.svg")
addIcon(regular,  997, "glyphs/DIN0997_Drehzahl_regeln.svg")
#Page 27
addIcon(regular, 1002, "glyphs/DIN1002_Endschalter_allgemein.svg", "Endschalter, allgemein")
addIcon(regular, 1003, "glyphs/DIN1003_Walzen_schließen_Walzen_zusammenfahren.svg", "Walzen schließen; Walzen zusammenfahren")
addIcon(regular, 1004, "glyphs/DIN1004_Walzen_abheben_Walzen_auseinanderfahren.svg", "Walzen abheben; Walzen auseinanderfahren")
addIcon(regular, 1019, "glyphs/DIN1019_Linksdrehung_Linkslauf.svg", "Linksdrehen; Linkslauf")
addIcon(regular, 1024, "glyphs/DIN1024_Untere_Walze_anlegen.svg")
addIcon(regular, 1025, "glyphs/DIN1025_Obere_Walze_anlegen.svg")
addIcon(regular, 1040, "glyphs/DIN1040_Schwerkraftabscheider_allgemein.svg", "Schwerkraftabscheider, allgemein")
addIcon(regular, 1041, "glyphs/DIN1041_Schwerkraft_Gegenstromabscheider.svg", "Schwerkraft-Gegenstromabscheider")
addIcon(regular, 1042, "glyphs/DIN1042_Schwerkraft_Querstromabscheider.svg", "Schwerkraft-Querstromabscheider")
addIcon(regular, 1043, "glyphs/DIN1043_Schwerkraft_Umlenkabscheider.svg", "Schwerkraft-Umlenkabscheider")
#Page 29
addIcon(regular, 1109, "glyphs/DIN1109_Vorbereitendes_Schalten_auf_eine_vorzuwaehlende_Drehzahl.svg", "Vorbereitendes Schalten auf eine vorzuwählende Drehzahl")
addIcon(regular, 1110, "glyphs/DIN1110_Vorgewaehlte_Drehzahl_loeschen.svg", "Vorgewählte Drehzahl löschen")
addIcon(regular, 1111, "glyphs/DIN1111_Ingangsetzen_auf_vorgewaehlte_Drehzahl.svg", "Ingangsetzen auf vorgewählte Drehzahl")
addIcon(regular, 1118, "glyphs/DIN1118_Abstreifer_angestellt_angelegt_Rakel_angestellt_angelegt.svg", "Abstreifer angestellt, angelegt; Rakel angestellt, angelegt")
addIcon(regular, 1119, "glyphs/DIN1119_Abstreifer_abgestellt_abgehoben_Rakel_abgestellt_abgehoben.svg", "Abstreifer abgestellt, abgehoben; Rakel abgestellt, abgehoben")
addIcon(regular, 1127, "glyphs/DIN1127_Behaelter_gefuellt.svg", "Behälter gefüllt")
addIcon(regular, 1129, "glyphs/DIN1129_Behaelter_teilgefuellt.svg", "Behälter; teilgefüllt")
addIcon(regular, 1130, "glyphs/DIN1130_Behaelter_leer.svg", "Behälter leer")
addIcon(regular, 1153, "glyphs/DIN1153_Drehbewegung_in_Produktionsrichtung.svg")
addIcon(regular, 1154, "glyphs/DIN1154_Drehbewegung_entgegen_Produktionsrichtung.svg")
addIcon(regular, 1155, "glyphs/DIN1155_Unterbrochene_Drehbewegung_in_Produktionsrichtung.svg")
addIcon(regular, 1156, "glyphs/DIN1156_Unterbrochene_Drehbewegung_entgegen_Produktionsrichtung.svg")
#Page 31
addIcon(regular, 1222, "glyphs/DIN1222_Einlauf_in_die_Maschine.svg")
addIcon(regular, 1223, "glyphs/DIN1223_Auslauf_aus_der_Maschine.svg")
addIcon(regular, 1225, "glyphs/DIN1225_Walze_allgemein.svg", "Walze, allgemein")
addIcon(regular, 1226, "glyphs/DIN1226_Buerstwalze_abgehoben.svg", "Bürstenwalze abgehoben")
addIcon(regular, 1254, "glyphs/DIN1254_Fuehler_allgemein_Messort_Waechter.svg", "Fühler, allgemein; Meßort; Wächter")
addIcon(regular, 1261, "glyphs/DIN1261_Veraendern_einer_Warenbahnspannung_Fadenzug_mit_markierter_Ausgangsstellung.svg", "Verändern einer Warenbahnspannung; Fadenzugspannung mit markierter Ausgangsstellung")
addIcon(regular, 1265, "glyphs/DIN1265_Drehzahl_aendern.svg", "Drehzahl ändern")
addIcon(regular, 1279, "glyphs/DIN1279_Auge_Kontrollieren_Pruefen.svg", "Auge; Kontrollieren; Prüfen")
addIcon(regular, 1287, "glyphs/DIN1287E_Fluessig_sichern_Kleben_Dichten.svg", "Flüssig sichern; Kleben; Dichten")
addIcon(regular, 1293, "glyphs/DIN1293_Einoelen_Oel.svg", "Einölen; Öl")
#Page 33
addIcon(regular, 1384, "glyphs/DIN1384_Stand_zu_niedring.svg")
addIcon(regular, 1385, "glyphs/DIN1385_Stand_zu_hoch.svg")
#Page 35
addIcon(regular, 1416, "glyphs/DIN1416_Bewegung_rechtsdrehend_aus_einer_Begrenzung.svg")
addIcon(regular, 1418, "glyphs/DIN1418_Druckluftschaltung.svg")
addIcon(regular, 1420, "glyphs/DIN1420_Bewegung_linksdrehend_aus_einer_Begrenzung.svg")
addIcon(regular, 1429, "glyphs/DIN1429_Schaummittel.svg")
addIcon(regular, 1431, "glyphs/DIN1431_Netzmittel.svg")
addIcon(regular, 1480, "glyphs/DIN1480_Temperatur_zu_hoch.svg")
addIcon(regular, 1481, "glyphs/DIN1481_Temperatur_zu_niedrig.svg")
#Page 37

#Page 39
addIcon(regular, 1699, "glyphs/DIN1699_Nullpunktverschiebung.svg")
#Page 41
addIcon(regular, 1758, "glyphs/DIN1758_Veraendern_einer_Groesse_in_Stufen.svg", "Verändern einer Größe in Stufen")
addIcon(regular, 1781, "glyphs/DIN1781_Messwertaufnehmer.svg")
#Page 43
addIcon(regular, 1849, "glyphs/DIN1849_Start_tastend.svg", "Start, tastend")
addIcon(regular, 1900, "glyphs/DIN1900_Orientierter_Stop.svg")
#Page 45

#Page 47
addIcon(regular, 2051, "glyphs/DIN2051_Behaelterinhalt_austauschen.svg", "Behälterinhalt austauschen")
#Page 49
addIcon(regular, 2146, "glyphs/DIN2146_Drehrichtung_im_Uhrzeigersinn.svg")
addIcon(regular, 2159, "glyphs/DIN2159_Drehrichtung_entgegen_Uhrzeigersinn.svg")
addIcon(regular, 2187, "glyphs/DIN2187_Positionieren.svg")
addIcon(regular, 2200, "glyphs/DIN2200_Reinigung_automatisch.svg", "Reinigung, automatisch")
#Page 51
addIcon(regular, 2201, "glyphs/DIN2201_Nicht_betaetigen_nicht_eingreifen.svg", "Nicht betätigen; Nicht eingreifen")
#Page 53
addIcon(regular, 2301, "glyphs/DIN2301_Programm_ohne_Maschinen_Funktionen.svg", "Programm ohne Maschinen-Funktionen")
addIcon(regular, 2302, "glyphs/DIN2302_Programm_mit_Maschinen_Funktionen.svg", "Programm mit Maschinen-Funktionen")
addIcon(regular, 2303, "glyphs/DIN2303_Bezugspunkt.svg")
addIcon(regular, 2306, "glyphs/DIN2306_Veraendern.svg", "Verändern")
addIcon(regular, 2307, "glyphs/DIN2307_Programm_einlesen_ohne_Maschinen_Funktionen.svg", "Programm-Einlesen ohne Maschinen-Funktionen")
addIcon(regular, 2308, "glyphs/DIN2308_Programm_einlesen_mit_Maschinen_Funktionen.svg", "Programm-Einlesen mit Maschinen-Funktionen")
addIcon(regular, 2309, "glyphs/DIN2309_Satzweises_Einlesen_ohne_Maschinen_Funktionen.svg", "Satzweises einlesen ohne Maschinen-Funktionen")
addIcon(regular, 2310, "glyphs/DIN2310_Satzweises_Einlesen_mit_Maschinen_Funktionen.svg", "Satzweises einlesen mit Maschinen-Funktionen")
addIcon(regular, 2311, "glyphs/DIN2311_Programm_veraendern.svg", "Programm verändern")
addIcon(regular, 2312, "glyphs/DIN2312_Unterprogramm.svg")
addIcon(regular, 2315, "glyphs/DIN2315_Suchlauf_vorwaerts.svg", "Suchlauf vorwärts")
addIcon(regular, 2316, "glyphs/DIN2316_Suchlauf_rueckwaerts.svg", "Suchlauf rückwärts")
addIcon(regular, 2317, "glyphs/DIN2317_Satznummern_Suche_vorwaerts.svg", "Satznummern-Suche vorwärts")
addIcon(regular, 2318, "glyphs/DIN2318_Satznummern_Suche_rueckwaerts.svg", "Satznummern-Suche rückwärts")
addIcon(regular, 2319, "glyphs/DIN2319_Hauptsatz_Suche_vorwaerts.svg", "Hauptsatz-Suche vorwärts")
addIcon(regular, 2320, "glyphs/DIN2320_Hauptsatz_Suche_rueckwaerts.svg", "Hauptsatz-Suche rückwärts")
addIcon(regular, 2321, "glyphs/DIN2321_Satz_Unterdrueckung.svg", "Satz-Unterdrückung")
addIcon(regular, 2322, "glyphs/DIN2322_Programm_Anfang.svg", "Programm-Anfang")
addIcon(regular, 2323, "glyphs/DIN2323_Programm_Ende.svg", "Programm-Ende")
addIcon(regular, 2324, "glyphs/DIN2324_Programm_Ende_mit_Lochstreifen_Ruecklauf_bis_Programm_Anfang.svg", "Programm-Ende mit Lochstreifen-Rücklauf bis Programm-Anfang")
addIcon(regular, 2325, "glyphs/DIN2325_Suchlauf_rueckwaerts_zum_Programm_Anfang.svg", "Suchlauf rückwärts zum Programm-Anfang")
addIcon(regular, 2326, "glyphs/DIN2326_Programmierter_Halt.svg")
addIcon(regular, 2327, "glyphs/DIN2327_Wahlweiser_programmierter_Halt.svg")
addIcon(regular, 2330, "glyphs/DIN2330_Handeingabe.svg")
addIcon(regular, 2335, "glyphs/DIN2335_Absolute_Massangabe.svg")
addIcon(regular, 2336, "glyphs/DIN2336_Relative_Massangabe.svg")
addIcon(regular, 2337, "glyphs/DIN2337_Referenzpunkt.svg")
addIcon(regular, 2338, "glyphs/DIN2338_Gitterpunkt.svg")
addIcon(regular, 2339, "glyphs/DIN2339_Koordinaten_Nullpunkt.svg", "Koordinaten-Nullpunkt")
addIcon(regular, 2341, "glyphs/DIN2341_Senden_aus_Speicher.svg")
addIcon(regular, 2342, "glyphs/DIN2342_Empfangen_in_Speicher.svg")
addIcon(regular, 2345, "glyphs/DIN2345_Nullpunkt_Korrektur.svg", "Nullpunkt-Korrektur")
addIcon(regular, 2346, "glyphs/DIN2346_Positioniergenaugikeit_fein.svg", "Positioniergenaugikeit, fein")
addIcon(regular, 2347, "glyphs/DIN2347_Positioniergenaugikeit_mittel.svg", "Positioniergenaugikeit, mittel")
addIcon(regular, 2348, "glyphs/DIN2348_Positioniergenauigkeit_grob.svg", "Positioniergenaugikeit, grob")
addIcon(regular, 2349, "glyphs/DIN2349_Datenaufzeichnung_in_einen_Speicher_Enter_Datenfreigabe.svg", "Datenaufzeichnung in einen Speicher; Enter (Datenfreigabe")
addIcon(regular, 2350, "glyphs/DIN2350_Daten_lesen_aus_einem_Speicher.svg")
addIcon(regular, 2362, "glyphs/DIN2362_Position.svg")
addIcon(regular, 2367, "glyphs/DIN2367_Bereit_fertig.svg", "Bereit, fertig")
addIcon(regular, 2371, "glyphs/DIN2371_Nicht_bereit.svg")
addIcon(regular, 2373, "glyphs/DIN2373_Testlauf.svg")
addIcon(regular, 2391, "glyphs/DIN2391_Programmmierbarer_Zeitgeber.svg")
#Page 55
addIcon(regular, 2401, "glyphs/DIN2401E_Verpackung_offen_leer_Papierbehaelter_leer_verfuegbar.svg", "Verpackung offen, leer; Papierbehälter leer, verfügbar")
addIcon(regular, 2402, "glyphs/DIN2402E_Verpackung_geschlossen_leer.svg", "Verpackung geschlossen, leer")
addIcon(regular, 2403, "glyphs/DIN2403E_Kein_Packmittel.svg")
addIcon(regular, 2404, "glyphs/DIN2404E_Verpackung_offen_gefuellt.svg", "Verpackung offen, gefüllt")
addIcon(regular, 2405, "glyphs/DIN2405E_Verpackung_geschlossen_gefuellt.svg", "Verpackung geschlossen, gefüllt")
addIcon(regular, 2406, "glyphs/DIN2406E_Deckel_Verschluss.svg", "Deckel, Verschluß")
addIcon(regular, 2407, "glyphs/DIN2407E_Deckel_fehlt_Verschluss_fehlt.svg", "Deckel fehlt; Verschluß fehlt")
addIcon(regular, 2409, "glyphs/DIN2409E_Becher_Behaeltnis.svg", "Becher, Behältnis")
addIcon(regular, 2410, "glyphs/DIN2410E_Kein_Becher_Kein_Behaeltnis.svg", "Kein Becher, kein Behältnis")
addIcon(regular, 2411, "glyphs/DIN2411E_Becher_Behaeltnis_Verschluss.svg", "Becher-, Behältnis-Verschluß")
addIcon(regular, 2412, "glyphs/DIN2412E_Bescherverschluss_anheften.svg")
addIcon(regular, 2434, "glyphs/DIN2434E_Fluessig.svg", "Flüssig")
addIcon(regular, 2439, "glyphs/DIN2439_Fuellhoehe_messen_Fuellstandskontrolle.svg", "Füllhöhe messen; Füllstandskontrolle")
addIcon(regular, 2440, "glyphs/DIN2440_Fuellhoehe_veraendern_Fuellmenge_veraendern.svg", "Füllhöhe verändern; Füllmenge verändern")
addIcon(regular, 2449, "glyphs/DIN2449_Durchflußregelung.svg")
addIcon(regular, 2450, "glyphs/DIN2450_Wasserbehaelter_Wasserbecken.svg", "Wasserbehälter, Wasserbecken")
addIcon(regular, 2451, "glyphs/DIN2451_Wassertemperatur.svg")
addIcon(regular, 2453, "glyphs/DIN2453_Heizung_geregelt.svg")
#Page 57
addIcon(regular, 2586, "glyphs/DIN2586_Druck_zu_hoch.svg")
addIcon(regular, 2587, "glyphs/DIN2587_Druck_zu_niedring.svg")
#Page 59
addIcon(regular, 2603, "glyphs/DIN2603_Wasserdruck.svg")
addIcon(regular, 2679, "glyphs/DIN2679_Stoff_Fluss_entgegen_Produktionsrichtung.svg", "Stoff-Fluß entgegen Produktionsrichtung (Gegenstromprinzip)")
addIcon(regular, 2680, "glyphs/DIN2680_Stoff_Fluss_in_Produktionsrichtung.svg", "Stoff-Fluß in Produktionsrichtung (Gleichstromprinzip")
addIcon(regular, 2692, "glyphs/DIN2692_Geschwindigkeitsregelung_m_min.svg", "Geschwindigkeitregelung m/min")
addIcon(regular, 2693, "glyphs/DIN2693_Vorbereitendes_Schalten_einer_Zeitspanne_in_Minuten.svg")
#Page 61
addIcon(regular, 2757, "glyphs/DIN2757_Filter_verschmutzt.svg")
#Page 63

#PAge 65
addIcon(regular, 2913, "glyphs/DIN2913_Wasserzulauf.svg")
addIcon(regular, 2959, "glyphs/DIN2959_Kundendienst_rufen.svg")
addIcon(regular, 2960, "glyphs/DIN2960_Toner_trocken_nachfuellen.svg", "Toner (trocken) nachfüllen")
addIcon(regular, 2961, "glyphs/DIN2961_Farbe_nachfuellen.svg", "Farbe nachfüllen")
addIcon(regular, 2962, "glyphs/DIN2962_Toner_fluessig_nachfuellen.svg", "Toner (flüssig) nachfüllen")
addIcon(regular, 2963, "glyphs/DIN2963_Dispersant_nachfuellen.svg", "Dispersant nachfüllen")
addIcon(regular, 2964, "glyphs/DIN2964_Entwickler_nachfuellen_gebrauchsfertig.svg", "Entwickler nachfüllen (gebrauchsfertig)")
addIcon(regular, 2965, "glyphs/DIN2965_Wasser_nachfuellen.svg", "Wasser nachfüllen")
addIcon(regular, 2979, "glyphs/DIN2979_Blatt_Seite_markieren.svg", "Blatt/Seite markieren")
addIcon(regular, 2980, "glyphs/DIN2980_Blatt_Seite_wieder aufrufen_Markierte_Seite_wieder_aufrufen.svg", "Blatt/Seite wieder aufrufen; Markierte Seite wieder aufrufen")
addIcon(regular, 2993, "glyphs/DIN2993_Recovery_Recycling_allgemein.svg", "Recovery/Recycling, allgemein")
#Page 67

#Page 69
addIcon(regular, 3103, "glyphs/DIN3103_Rotationsbuerste.svg", "Rotationsbürste")
#Page 71
addIcon(regular, 3245, "glyphs/DIN3245_Grenzwerte_allgemein.svg", "Grenzwerte, allgemein")
addIcon(regular, 3246, "glyphs/DIN3246_Oberen_Grenzwert_verstellen.svg")
addIcon(regular, 3247, "glyphs/DIN3247_Unteren_Grenzwert_verstellen.svg")
addIcon(regular, 3239, "glyphs/DIN3239_Menue_aufrufen.svg", "Menü aufrufen")
addIcon(regular, 3269, "glyphs/DIN3269_Mischen.svg")
addIcon(regular, 3271, "glyphs/DIN3271_Ruecksetzen_in_den_Ausgangszustand.svg", "Rücksetzen in den Ausgangszustand")
addIcon(regular, 3272, "glyphs/DIN3272_Annullierung_vollstaendig.svg", "Annullierung, vollständig")
addIcon(regular, 3280, "glyphs/DIN3280_Einstellen_der_Basislinie_auf_vorgegebenen_Wert.svg")
addIcon(regular, 3296, "glyphs/DIN3296_Bewegung_handbetaetigt.svg", "Bewegung, handbetätigt")
#Page 73
addIcon(regular, 3328, "glyphs/DIN3328_Elektronische_Berechtigung.svg")
addIcon(regular, 3330, "glyphs/DIN3330_Information.svg")
#Page 75
addIcon(regular, 3403, "glyphs/DIN3403_Funktionsstoerung_allgemein.svg", "Funktionsstörung, allgemein")
#Page 77
addIcon(regular, 3559, "glyphs/DIN3559_Wasserzulauf_offen.svg")
#Page 79
addIcon(regular, 3663, "glyphs/DIN3663_Waermestrahlung_von_Warenbahn_abgewendet.svg", "Wärmestrahlung von Warenbahn abgewendet")
addIcon(regular, 3664, "glyphs/DIN3664_Waermestrahlung_auf_Warenbahn_gerichtet.svg", "Wärmestrahlung auf Warenbahn gerichtet")
addIcon(regular, 3677, "glyphs/DIN3677_Geschwindigkeitsdifferenz_in_Prozent.svg", "Geschwindigkeitsdifferenz in %")
addIcon(regular, 3678, "glyphs/DIN3678_Geschwindigkeitsdifferenz_hundert_Prozent.svg", "Geschwindigkeit 100 %")
#Page 81
addIcon(regular, 3764, "glyphs/DIN3764_Ausschaltzeit.svg")
addIcon(regular, 3765, "glyphs/DIN3765_Einschaltzeit.svg")
addIcon(regular, 3766, "glyphs/DIN3766_Betriebsdauer.svg")
addIcon(regular, 3798, "glyphs/DIN3798_Schreiben_in_den_Datenspeicher_beenden.svg")
#Page 83
addIcon(regular, 3813, "glyphs/DIN3813_Anzeige_der_verbleibenden_Zeit.svg")
addIcon(regular, 3814, "glyphs/DIN3814_Anzeige_der_abgelaufenen_Zeit.svg")
addIcon(regular, 3846, "glyphs/DIN3846_NotAus.svg", "NOT-AUS")
addIcon(regular, 3882, "glyphs/DIN3882_Vorherige_Seite.svg", "Vorherige Seite (eines Textteiles)")
addIcon(regular, 3883, "glyphs/DIN3883_Naechste_Seite.svg", "Nächste Seite (eines Textteiles)")
#Page 85
addIcon(regular, 3903, "glyphs/DIN3903_Eingang_Ausgang.svg", "Eingang/Ausgang")
#Page 87




# export to files
flags = ("opentype", "dummy-dsig", "round", "apple")
regular.generate ("out/DIN_30600.ttf", flags=flags)
regular.close()
