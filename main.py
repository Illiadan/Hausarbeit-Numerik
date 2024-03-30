# -------------------------------------------------------------
# ----------------------IMPORTS--------------------------------
# -------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

import exakt
import gaußLegendre
import simpson
import trapez

# -------------------------------------------------------------
# ----------------------SETUP----------------------------------
# -------------------------------------------------------------

fx = lambda x: np.cos(3. * x) * np.exp(-x / 2.) - np.sin(x)  # Funktion
a = 0  # untere Intervallgrenze
b = 3  # obere Intervallgrenze
nTS = [8, 16, 32]  # Unterteilungen Trapez/Simpson
nGL = [6, 8, 10, 16]  # Stützstellen Gauß Legendre

# -------------------------------------------------------------
# ----------------------FUNCTIONS------------------------------
# -------------------------------------------------------------

ex = exakt.exakt(fx, a, b)
trapez8 = trapez.trapez(fx, a, b, nTS[0])
trapez16 = trapez.trapez(fx, a, b, nTS[1])
trapez32 = trapez.trapez(fx, a, b, nTS[2])
simpson8 = simpson.simpson(fx, a, b, nTS[0])
simpson16 = simpson.simpson(fx, a, b, nTS[1])
simpson32 = simpson.simpson(fx, a, b, nTS[2])
gl6 = gaußLegendre.gaußLegendre(fx, a, b, nGL[0])
gl8 = gaußLegendre.gaußLegendre(fx, a, b, nGL[1])
gl10 = gaußLegendre.gaußLegendre(fx, a, b, nGL[2])
gl16 = gaußLegendre.gaußLegendre(fx, a, b, nGL[3])

# -------------------------------------------------------------
# ----------------------OUTPUT---------------------------------
# -------------------------------------------------------------

print("################################################################################")
print("################################## HAUSARBEIT ##################################")
print("################################################################################")
print("\nAutor: Junghans, Martin                          Kurs: BA Leipzig, MA4NU, CS19-1\n")
print("---------------------------------")
print("Vorbetrachtung (Aufgabe 1, 2, 3):")
print("---------------------------------")
print("\nFunktionsgleichung:  f(x):=cos(3x)e^(x/2)-sin(x)")
print("\nIntegralsberechnung im Intervall 0 <= x <= 3")
print("\nIntegralsberechnung mittels:\n  - Trapez-Regel\n  - Simpson-Regel\n  - Gauß-Integration mit Legendre Polynomen\n")
print("----------------------------------------------")
print("Aufgabe 4: Grafische Darstellung der Funktion")
print("----------------------------------------------")
print("""\nEs sollte sich ein weiteres Fenster \"Figure 1\" geöffnet haben.
    \nDie obere Darstellung soll helfen ein besseres Gefühl für den Kurvenverlauif zu bekommen.
    \nDaher ist die gegebene Funktion hier im Intervall [-5;5] dargestellt.
    \nDie untere Darstellung zeigt die Funktion im deklarierten Intervall [0;3],
    \nwobei die wertmäßig positiven und negativen Flächen unter bzw. über der Kurve farblich hervorgehoben wurden.\n
""")
print("--------------------------------------------------------")
print("Aufgabe 5: Integration mittels Trapez- und Simpson-Regel")
print("--------------------------------------------------------")
print("\nLösungen Trapez-Regel:")
print("------------------------")
print("\nn=8: {outT}".format(outT=trapez8.approx))
print("n=16: {outT}".format(outT=trapez16.approx))
print("n=32: {outT}".format(outT=trapez32.approx))
print("\nLösungen Simpson-Regel:")
print("-------------------------")
print("\nn=8: {outT}".format(outT=simpson8.approx))
print("n=16: {outT}".format(outT=simpson16.approx))
print("n=32: {outT}\n".format(outT=simpson32.approx))
print("""\nUnterstützend zu den schriftlichen Ausführungen wurde der Vergleich
    \nder absoluten Fehler in \"Figure 2\" grafisch dargestellt.\n
""")
print("----------------------------------------------------")
print("Aufgabe 6: Integration mittels Gauß-Legendre-Methode")
print("----------------------------------------------------")
print("\nn=6: {outGL}".format(outGL=gl6.approx))
print("n=8: {outGL}".format(outGL=gl8.approx))
print("n=10: {outGL}".format(outGL=gl10.approx))
print("n=16: {outGL}\n".format(outGL=gl16.approx))
print("""
\"Figure 3\" zeigt das Fehlerverhalten der in Abhängigkeit zur
    \nAnzahl der Stützstellen n.\n
""")
print("---------------------------------------")
print("Aufgabe 7: Exaktes Integrationsergebnis")
print("---------------------------------------")
print("\nexaktes Ergebnis: {out}".format(out=ex[0]))

# -------------------------------------------------------------
# ----------------------DIAGRAMS-------------------------------
# -------------------------------------------------------------

x = np.linspace(-5, 5, 1000)
x1 = np.linspace(0, 3, 1000)

general = plt.figure(1)
plt.subplot(211)
plt.plot(x, fx(x), "darkorchid")
plt.title("cos(3x) * exp(-x/2) - sin(x)")
plt.xlabel("x")
plt.ylabel("y=f(x)")
plt.grid(True)
plt.axis([-5, 5, -12.5, 10])
plt.xticks(np.arange(min(x), max(x) + 1, 1.0))

interval = plt.figure(1)
plt.subplot(212)
plt.plot(x1, fx(x1), "darkorchid")
plt.title("cos(3x) * exp(-x/2) - sin(x)")
plt.xlabel("x")
plt.ylabel("y=f(x)")
plt.grid(True)
plt.axis([0, 3, -1.5, 1.5])
plt.xticks(np.arange(min(x1), max(x1) + 0.25, 0.25))
plt.yticks(np.arange(-2, 2, 0.5))
plt.fill_between(x1, 0, fx(x1), where=fx(x1) > 0, facecolor="lightblue")
plt.fill_between(x1, 0, fx(x1), where=fx(x1) < 0, facecolor="lightsalmon")
plt.tight_layout()

compareTS = plt.figure(2)
plt.plot(nTS, [np.abs(trapez8.approx - ex[0]), np.abs(trapez16.approx - ex[0]),
               np.abs(trapez32.approx - ex[0])], "ro", label="Trapez")
plt.plot(nTS, [np.abs(simpson8.approx - ex[0]), np.abs(simpson16.approx - ex[0]),
               np.abs(simpson32.approx - ex[0])], "go", label="Simpson")
plt.title("Vergleich Trapez/Simpson in Abhängigkeit von n")
plt.xlabel("n")
plt.ylabel("I[f]_Trapez/Simpson - I[f]_exakt")
plt.grid(True)
plt.axis([7, 33, -0.000001, 0.03])
plt.xticks(np.arange(8, 40, 8))
plt.yticks(np.arange(-0.005, 0.03, 0.005))
plt.legend()
plt.tight_layout()

compareGL1 = plt.figure(3)
plt.plot(nGL, [np.abs(gl6.approx - ex[0]), np.abs(gl8.approx - ex[0]),
               np.abs(gl10.approx - ex[0]), np.abs(gl16.approx - ex[0])], "ro")
plt.title("Verhalten (Gauß) in Abhängigkeit von n")
plt.xlabel("n")
plt.ylabel("I[f]_Gauß - I[f]_exakt")
plt.grid(True)
plt.axis([5, 17, -0.000001, 0.000063])
plt.xticks(np.arange(6, 18, 2))
plt.yticks(np.arange(-0.00001, 0.000063, 0.00001))
plt.tight_layout()

plt.show()

# -------------------------------------------------------------
# ----------------------EXE NECESSITIES------------------------
# -------------------------------------------------------------

input("\n\nZum Beenden ENTER drücken...\nPress ENTER to quit ...")
