text = "DAX unter 15.000 Punkten -- Asiens Börsen schließen in Rot -- Bayer meldet Erfolg in Glyphosat-Prozess -- TUI will mit Kapitalerhöhung Milliardenbetrag an Schulden abbauen -- SYNLAB, Facebook im Fokus - finanzen.net"
titleArr = text.split()
back = ""
temp = ""
for x in titleArr:
    if len(temp+x) > 60:
        back += temp + "\n"
        temp = x
    else:
        temp += x + " "
back += temp + "\n"
print(back)