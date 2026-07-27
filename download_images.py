import os
import shutil
from bing_image_downloader import downloader

# The dictionary matching the search query to your exact HTML filename
villains_to_download = {
    "Darth Vader movie": "darth_vader.jpg",
    "The Joker Batman movie": "joker.jpg",
    "Hannibal Lecter Silence of the Lambs": "hannibal_lecter.jpg",
    "Lord Voldemort Harry Potter": "voldemort.jpg",
    "Sauron Lord of the Rings movie": "sauron.jpg",
    "Norman Bates Psycho movie": "norman_bates.jpg",
    "Anton Chigurh No Country for Old Men": "anton_chigurh.jpg",
    "Thanos Marvel cinematic universe": "thanos.jpg",
    "Emperor Palpatine Star Wars": "palpatine.jpg",
    "Magneto X-Men movie": "magneto.jpg",
    "Lex Luthor Superman movie": "lex_luthor.jpg",
    "Wicked Witch of the West Wizard of Oz": "wicked_witch.jpg",
    "Michael Myers Halloween movie": "michael_myers.jpg",
    "Freddy Krueger Nightmare on Elm Street": "freddy_krueger.jpg",
    "Jason Voorhees Friday the 13th": "jason_voorhees.jpg",
    "T-800 Terminator movie": "t800.jpg",
    "Gollum Lord of the Rings movie": "gollum.jpg",
    "Scar Lion King movie": "scar.jpg",
    "Joffrey Baratheon Game of Thrones": "joffrey_baratheon.jpg",
    "Night King Game of Thrones": "night_king.jpg",
    "Homelander The Boys TV": "homelander.jpg",
    "Gus Fring Breaking Bad": "gus_fring.jpg",
    "Negan The Walking Dead": "negan.jpg",
    "Bowser Super Mario": "bowser.jpg",
    "Ganondorf Legend of Zelda": "ganondorf.jpg",
    "Albert Wesker Resident Evil": "albert_wesker.jpg",
    "Dracula movie": "dracula.jpg",
    "Lich King World of Warcraft": "lich_king.jpg",
    "Nemesis Resident Evil 3": "nemesis.jpg",
    "Pyramid Head Silent Hill 2": "pyramid_head.jpg",
    "Ridley Metroid": "ridley.jpg",
    "Maleficent Sleeping Beauty": "maleficent.jpg",
    "Ursula The Little Mermaid": "ursula.jpg",
    "Jafar Aladdin": "jafar.jpg",
    "Gaston Beauty and the Beast": "gaston.jpg",
    "Yzma Emperor's New Groove": "yzma.jpg",
    "Kylo Ren Star Wars": "kylo_ren.jpg",
    "General Grievous Star Wars": "general_grievous.jpg",
    "Green Goblin Spider-Man movie": "green_goblin.jpg",
    "Doctor Octopus Spider-Man movie": "doctor_octopus.jpg",
    "Venom Spider-Man movie": "venom.jpg",
    "Loki Marvel MCU": "loki.jpg",
    "Hela Thor Ragnarok": "hela.jpg",
    "Ultron Avengers movie": "ultron.jpg",
    "Bane Batman movie": "bane.jpg",
    "Pennywise IT movie": "pennywise.jpg"
}

# Create the images directory if it doesn't exist
os.makedirs("images", exist_ok=True)

print("Starting automated image downloads...")

for search_query, filename in villains_to_download.items():
    print(f"Fetching image for {search_query}...")
    
    # Download 1 high-quality image per query into a temporary folder
    downloader.download(
        search_query, 
        limit=1,  
        output_dir='temp_images', 
        adult_filter_off=False, 
        force_replace=False, 
        timeout=60, 
        verbose=False
    )
    
    # The downloader creates a subfolder named after the query. 
    # We need to grab the downloaded image, rename it, and move it to your 'images' folder.
    query_folder = os.path.join('temp_images', search_query)
    
    if os.path.exists(query_folder):
        downloaded_files = os.listdir(query_folder)
        if downloaded_files:
            # Grab the first file downloaded
            downloaded_img_path = os.path.join(query_folder, downloaded_files[0])
            final_dest_path = os.path.join('images', filename)
            
            # Move and rename it to exactly match your HTML file's expectations
            shutil.move(downloaded_img_path, final_dest_path)
            print(f"Successfully saved {filename}")

# Clean up the temporary folder after we've moved everything
if os.path.exists('temp_images'):
    shutil.rmtree('temp_images')

print("All done! Your 'images' folder is populated.")
