# --- Imports ---
import sys, os, time
from ASCII_arts_col import ascii #ASCII art dictionary
from type_writing_script import typew #Typewriting machine effect
import Actions
# --- Title & intro ---
print (ascii.get('title')) #game title

    # --- Story backstory ---
typew ("\nIt's been more than a year since Demonic Plague emerged in west Vateria. Demon Warlords \nmarched their armies through Null Point, what most call Hell's Gates. Under the patronage of \nLucius of Underworld, they rapidly advanced into Talayir, shocking nearby nations. \nHaphazardly they formed anti-devil alliance, once opponents became allies against the biggest \nthreat Talayir has ever seen.\n")

    # --- Character creation ---
print ("\nWhat is your name?")
name = input('> ')
pname = "Private " + name

    # --- Story ---
typew(f"\nYou're a scout soldier from Kingdom of Alverland. Your task is to deliver a valuable intel to \nunited command. Reading the intel is prohibited. The route will start from west front, near the \nriver Khurik, after which you have to move north, through trenches of Blauvald, mountains \nand forests of Äscalia, until you reach north front command center in Amania. May the God \nhelp you in this mission, {pname}.\n")

# --- Chapter 1 ---

