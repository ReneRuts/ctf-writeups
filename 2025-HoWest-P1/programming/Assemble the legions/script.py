import os

legions = {
    "Dark Angels": "Lion El Johnson",
    "Emperors Children": "Fulgrim",
    "Iron Warriors": "Perturabo",
    "White Scars": "Jaghatai Khan",
    "Space Wolves": "Leman Russ",
    "Imperial Fists": "Rogal Dorn",
    "Night Lords": "Konrad Curze",
    "Blood Angels": "Sanguinius",
    "Iron Hands": "Ferrus Manus",
    "World Eaters": "Angron",
    "Ultramarines": "Roboute Guilliman",
    "Death Guard": "Mortarion",
    "Thousand Sons": "Magnus the Red",
    "Sons of Horus": "Horus",
    "Word Bearers": "Lorgar",
    "Salamanders": "Vulkan",
    "Raven Guard": "Corvus Corax",
    "Alpha Legion": "Alpharius Omegon",
    "REDACTED": "REDACTED",
    "RECORDS REDACTED": "RECORDS REDACTED"
}

main_folder = "Adaptus_Astartes"
os.makedirs(main_folder, exist_ok=True)

for legion, primarch in legions.items():
    legion_folder = os.path.join(main_folder, legion)
    os.makedirs(legion_folder, exist_ok=True)
    
    primarch_file = os.path.join(legion_folder, f"{primarch}")
    with open(primarch_file, 'w') as f:
        f.write(primarch)

print(f"Folder structure created successfully under '{main_folder}'!")