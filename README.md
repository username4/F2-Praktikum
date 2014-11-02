F2-Praktikum, vom F1-Praktikum kopiert
==========

Protokolle und Vorbereitungen für das Fortgeschrittenen-Praktikum in der Physik (P4) am KIT

Für jeden Versuch sollte ein eigener Ordner erstellt werden. Leerzeichen sind zu vermeiden und am besten ist Kleinschreibung und kurze Ordnernamen, um die Arbeit von der Kommandozeile aus zu erleichtern. Für die Versuchsvorbereitung kann ein eigener Unterordner erstellt werden.

Die ".gitignore" Datei enthält Dateien, die von git nicht beobachtet werden soll, wie zum Beispiel kompilierte PDFs. Bitte keine PDFs zu den Commits hinzufügen. Also KEIN "git add *.pdf". Ebenso keine temporären Dateien oder Dateien, die beim Kompilieren entstehen, wie zum beispiel .aux und .toc. All diese Dateien sind im gitignore. Eine Ausnahme sind PDF-Dateien mit Vorbereitungsunterlagen bzw der Aufgabenstellung. Dann bitte "git add -f aufgabenstellung.pdf" verwenden.S 12 1 3


Die Bearbeitung von Praktikumsprotokollen mithilfe von git ist experimentell. Zuerst werde ich meine Teile hier commiten, daher sind die Protokolle hier nicht vollständig. Die offiziellen, vollständigen Versionen der Protokolle sind in der Dropbox. Wenn er Lust dazu bekommt, kann username4, mein Partner, aber ebenfalls hier commiten. Jedoch macht das erst wirklich Sinn, wenn immer wieder kleine Änderungen commitet werden. Wenn man zu selten commitet, entsteht die Gefahr von merge conflicts, also dass wir beide dieselbe Stelle bearbeitet haben.

==========
Wichtige git-Befehle:
(weitere Befehle und Infos unter "http://gitref.org")

- git init: erstelle neues repository im aktuellen Ordner
- git clone <name des repositories": erstelle Kopie eines Repositories 
- git status: anzeigen, welche Dateien geändert wurden und welche zum Commit vorgemerkt sind
- git add "Dateiname": Datei für den nächsten commit vormerken ("stagen"). Bitte keine kompilierten PDFs adden. Fuer PDF-Unterlagen lässt sich die gitignore-Sperre mit "git add -f foo.pdf" überwinden 
- git commit -m "Kommentar": Alle geänderten und vorgemerkten Dateien commiten mit Kommentar
- git log: log aller Commits anzeigen
- git diff: zeige Differenz der geänderten, aber nicht vorgemerkten Dateien zum letzten Commit an.
- git diff HEAD: zeige Differenz ALLER geänderten Dateien, egal ob vorgemerkt oder nicht, zum letzten Commit an.

- git branch "branchname": erstelle alternative Abzweigung vom akteullen Repo, kann später ge-merged (zusammengefügt) werden
- git branch: zeige alle Abzweigungen an. Die Default-Branch heißt "Master". Die aktuelle Branch ist mit "*" markiert.
- git checkout "branchname": wechsele zu einer anderen branch, um diese dann zu bearbeiten. 

!!! Git-Befehle zum Arbeiten mit dem github-repository:

- git add remote "remote-alias" "url": 
Füge ein remote repository zu deinem Projekt hinzu. Ganz konkret ist das hier das github-Repository, das halt online   auf einem server ist, parallel zu deinem eigenen Repository auf deinem Computer. Die URL ist folgende:
"https://github.com/username4/F2-Praktikum/". Man kann z.B. schreiben:
"git add remote fpraktikum@github https://github.com/username4/F2-Praktikum/"

- git remote: zeige alle remote repositories zum lokalen repo an
- git fetch "remote-alias": Lade Daten von einem remote repo herunter. Kann dann mit "git merge" zur aktuellen branch gemerged werden. Einfacher ist die Benutzung von git pull.
- git pull "remote-alias" "master": Lade Daten von einem remote-repo runter und merge sie mit der master-branch. Das ist das, was ich meistens benutze statt "git fetch".
- git push "remote-alias" "branchname": Lade deine eigenen commiteten Änderungen von branch auf das remote-repo hoch, konkret ist das hier z.B.: "git push fpraktikum@github master", da Master die default branch ist.

