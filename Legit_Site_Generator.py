import os
import csv
import ast
from pathlib import Path

#Set the optupt directory to your specified path
output_dir = Path("/Users/aaronhaverinen/Documents/Science Project Folder 2025/Site Generator")
csv_path = Path("/Users/aaronhaverinen/Documents/Science Project Folder 2025/Site Generator/Black Magic website - San Diego Info.csv")
required_cols = {"filemname", "title", "description", "image", "taxonomy", "stylesheet"}
image_root = "/"
print(csv_path)

#Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    print("Directory doesn't exist; creating one now at", output_dir)
    os.makedirs(output_dir)
def parse_list_cell(cell:str) -> list[str]:
    cell = (cell or "").strip()
    if not cell:
        return[]
    
    #Try a real list literal first
    try:
        parsed = ast.literal_eval(cell)
        if isinstance(parsed,str):
            return [parsed.strop()]
        if isinstance(parsed,list):
            return[str(item).strip() for item in parsed if str(item).strip()]
    except (SyntaxError, ValueError):
        pass
    
    #Accept bracket-wrapped shorthand
    if cell.startswith("[") and cell.endswith("]"):
        cell = cell[1:-1]
    
    return [part.strip() for part in cell.split(",") if part.strip()]

def csv_to_exhibits(csv_file: str | Path) -> list[dict]:
    csv_file = Path(csv_file)
    exhibits: list[dict] = []

    with csv_file.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        #missing = required_cols - set(reader.fieldnames of [])
        #if missing:
            #raise ValueError(f"CSV is missing required columns: {', '.join(missing)}")
        
        for row in reader:
            exhibits.append(
                {
                    "filename": row["filename"].strip(),
                    "title": row["title"].strip(),
                    "description": row["description"].strip(),
                    "image": parse_list_cell(row["image"]),
                    "stylesheet": row["stylesheet"].strip(),
                    **(
                        {"taxonomy": parse_list_cell(row["taxonomy"])}
                        if row.get("taxonomy", "").strip()
                        else{}
                    ),
                }
            )
    return exhibits


#exhibits = [
    # {
    #     "filename": "exhibit 1.html",
    #     "title": "Exhibit 1: Porifera",
    #     "description": "Though it may not seem as such, sea sponges are actually animals, and not plants. Sailors used to collect them to make dishwashing equipment (what now is synthetic). Now, porifera are mostly asymmetrical, reproducing both sexually and asexually. But this seems a bit strange. How can an animal reproduce both sexually and asexually? Well actually, asexual reproduction with porifera (or sponges) works via fragmentation, budding, or gemmules. Sexual reproduction occurs through releasing sperm or egg cells, where they float through the water to find another sponge, fertilizing it. However, sponges don't have true tissues or organs and are sessile, meaning not moving. Some fun facts about porifera are that they are filter-feeders, meaning that they filter water through themselves to extract the solids dissolved (i.e. plankton). This beauty above is the Giant Barrel Sponge, also known scientifically (or by its fancy name), <i>Xestospongia muta</i>. Their habitat is along the Caribbean and Gulf of America, most commonly on coral reefs. The Giant Barrel Sponge has a really long life span of around 2000 years! That means some sponges that are still living in our ocean today may have been alive when Jesus was doing his ministry! The Giant Barrel Sponge feeds on bacteria, plankton, prochlorophytes, and really any other nutrition dissolved in the water. It is not that picky. Another fun fact about sponges is that they are called porifera because of their many pores. Below is the taxonomy.",
    #     "image": [
    #         "Images of Animals/Giant_Barrel_Sponge.png", #Images of Porifera
    #     ],
    #     "taxonomy": ["Images of Animals/Poriferatax.png"],
    #     "stylesheet": "Exhib1.css"
    # }, 
    # {
    #     "filename": "exhibit 2.html",
    #     "title": "Exhibit 2: Cnidaria",
    #     "description": "Cnidaria is just a fancy Latin word for this phylum, which includes jellyfish, corals, and many others. Cnidaria are unique because they are the only phylum that has both the medusa and polyp stages. If you do not know what this means, it is completely OK. A jellyfish will start from an egg, then grow into a polyp, attached to the ground and commonly mistaken as a plant or even sponge, and then finally grow into a medusa with its large bell and tentacles. Cnidaria, like sponges, produce both sexually and asexually too. The asexual way works with budding, where the cnidarian can break off a bit of its body and then grow a new cnidarian out of it. Sexual reproduction works similarly to other animals by releasing sperm to fertilize females. Cnidaria also have tentacles, whose purpose is to sting and catch prey. This serves as an advantage to being a predator in the ocean. A funny fact about cnidaria is that they look like mushrooms. The cnidarian I've decided to showcase today is the Lion's Mane Jellyfish, also known by its boring name, the <i>Cyanea capillata</i>. This humongous jellyfish can grow tentacles as long as a hundred feet and its bell's circumference up to thirty feet! It lives in the cold waters of the Arctic, North Atlantic, and North Pacific Oceans. However, this glorious jellyfish only lives about twelve months, which is nothing compared to some other sea creatures. Its diet consists of zooplankton, small fish, and maybe even some other jellyfish occasionally. Below is the taxonomy.",
    #     "image": [
    #         "Images of Animals/Lions_Mane_Jellyfish.png"
    #     ],
    #     "taxonomy":["Images of Animals/Cnidariatax.png"], #Images of Cnidaria
    
    #     "stylesheet": "Exhib2.css"
    # },
    # {
    #     "filename": "exhibit 3.html",
    #     "title": "Exhibit 3: Mollusca",
    #     "description": "These are mollusca, a phylum that you're probably a bit familiar with. Their symmetry pattern is bilateral. Mollusca differ from other phyla because they actually have multiple hearts in their open circulatory system. Mollusca reproduce sexually through external fertilization, unlike most animals who reproduce internally. Some mollusks have shells and some do not, but all of them do have a mantle for protection. Above, I am showcasing the Giant Pacific Octopus, also known scientifically as the <i>Enteroctopus dofleini</i>. Their lifespan is around 3–5 years in the Pacific Ocean. Also, the Giant Pacific Octopus' diet can range from shrimp and crab to lobster and even more. As some fun facts, octopuses in general can change their color to camouflage with surroundings and can squirt ink to get away from enemies. And also, this specific octopus has nine brains! It has one central one for control and dominion over the other eight, which control each arm. How lucky. Imagine how much more innovation there would be if we each had nine brains! I'm just joking. Below is the taxonomy.",
    #     "image": [
    #         "Images of Animals/Giant_Pacific_Octopus.png"
    #     ],
    #     "taxonomy": ["Images of Animals/Molluscatax.png"], #Images of Mollusca
        
    #     "stylesheet": "Exhib3.css"
    # },
    # {
    #     "filename": "exhibit 4.html",
    #     "title": "Exhibit 4: Annelida",
    #     "description": "Now this phylum has a weird name (not saying that the others don't but yeah), annelida. There's nothing really too <i>special</i> about them, though they can see light without even any eyes and they breathe through a moist layer of water on their skin. That's why you can see that earthworms die when dried in the sun for a while. Annelids have bilateral symmetry and reproduce sexually, even though they are both genders at once! They rub against each other and exchange DNA to keep the line going. Their circulatory system is closed with some sort of heart-like structure. Their digestive system is complete, running all the way from their mouth to anus. Now this annelid that I have decided to show all of you today is the Red Tiger Worm, the <i>Eisenia andrei</i> (named by some scientists). This worm lives for around 5 years, usually residing in composts or dung heaps, or sometimes underground. It eats basically any decomposing matter it can find, usually some sort of produce. There really isn't much else to say. Below is the taxonomy.",
    #     "image": [
    #         "Images of Animals/Red_Earthworm.png"],
    #     "taxonomy": ["Images of Animals/Annelidatax.png"], #Images of Annelida
        
        
    #     "stylesheet": "Exhib4.css"
    # },
    # {
    #     "filename": "exhibit 5.html",
    #     "title": "Exhibit 5: Arthropoda",
    #     "description": "I'm certain that you have encountered this phylum before, but maybe not its name. This is arthropoda and it carries a very wide variety of creatures, in fact, so wide that this is the largest phylum, carrying more than 85 percent of all animal creatures! This phylum carries insects, crustaceans, and many others that could be crawling in your backyard, or living on the ocean floor. Now, this phylum has bilateral symmetry, with an open circulatory system. Their circulatory system runs on hemolymph, which is somewhat similar to blood, just a bit different and they pump it though their one-chambered heart. Arthropods' reproduction system occurs through internal fertilization, which means the reproduction is sexual. Arthropods also have a unique outer shell called an exoskeleton. This fancy word describes their hard outer covering, which can be used for protection, support, and a surface for muscle attachment. Metamorphosis is something that happens when arthropods start to grow, which has two types: incomplete and complete. Complete metamorphosis has four stages, starting from an egg, then hatching into the larva, then growing into a pupa, then turning into a fully-grown adult. Incomplete metamorphosis has only three steps, replacing the larva and pupa stages with just a nymph. A nymph is basically an immature adult, an altered version and younger. The arthropod that I'd like to show today is the American Lobster, or <i>Homarus americanus</i>, which has incomplete metamorphosis. It lives for around 50–100 years in shallow, cold coastal areas that have saltwater. They are distributed along the Northeastern coast of the United States. Its diet consists mostly of dead animals, clams, crabs, urchins, and even more.",
    #     "image": [
    #         "Images of Animals/American_Lobster.png"],
    #     "taxonomy": ["Images of Animals/Arthropodatax.png"] #Images of Arthropods
    #     ,
    #     "stylesheet": "Exhib5.css"
    # },
    # {
    #     "filename": "exhibit 6.html",
    #     "title": "Exhibit 6: Echinodermata",
    #     "description": "Some people love this phylum and others think it's boring and there is nothing special. But honestly, echinodermata are one of the most fascinating creatures in the entire ocean. You may have seen them wash up on the beach and think that these are just some cool rocks or dead plants, but there is actually something much more to them. Echinodermata are not just the shell, but have skin too, hence their name which translates to <i>spikey skin</i>. These can include starfish, sand dollars and even sea urchins! Echinoderms have pentaradial symmetry (or just radial if you don't feel like saying it all) and reproduce sexually through external fertilization. They have a water vascular system as their circulatory system, where water flows through them for locomotion, feeding, respiration, et cetera. Their digestive system is quite interesting too. Some vent food from their mouth instead of secreting it from their anus. This is the Common Starfish, or <i>Asterias rubens</i>. These starfish (or sea stars) live in the waters of the Atlantic Ocean for around 5 to 10 years. Their diet is pretty carnivorous (meaning meat-eating), hosting mollusks like clams, mussels, and even barnacles.",
    #     "image": [
    #         "Images of Animals/Starfish.png"],
    #     "taxonomy":["Images of Animals/Echinotax.png"] #Images of Echinodermata
    #     ,
    #     "stylesheet": "Exhib6.css"
    # },
    # {
    #     "filename": "exhibit 7.html",
    #     "title": "Exhibit 7: Aves",
    #     "description": "This next phylum will be chordata, with our last five animals being classes of that phylum. The first class is Aves. Aves are the first class that I will show you of vertebrates. Aves have an closed circulatory system with bilateral symmetry, producing sexually through internal fertilizaiton. Aves have wings and are really the only phylum that can fly. The bird I am showcasing here is the Blue Jay, known as the <i>Cyanocitta cristata</i>. Their habitat is usually mixed woodlands in Northeastern America and their lifespan is around 7 years. The blue jay's diet consists of seeds, nuts, and insects.",
    #     "image": [
    #         "Images of Animals/Blue_Jay.png"],
    #     "taxonomy":["Images of Animals/Avestax.png"] #Images of Aves
    #     ,
    #     "stylesheet": "Exhib7.css"
    # },
    # {
    #     "filename": "exhibit 8.html",
    #     "title": "Exhibit 8: Reptiles",
    #     "description": "Reptiles aren't a phylum and are part of the phylum Chordata. Instead, reptiles are a class, and are also categorized with amphibians in a colloquial superclass herps (which is not a scientific classificatory name). Reptiles are symmetrical bilaterally and reproduce sexually through internal fertilization and are usually oviparous but sometimes can also be viviparous or ovoviviparous (a mouthful to say). Reptiles produce an amniotic egg, meaning that the egg provides shelter and doesn't need moisture (it is held inside the egg). Reptiles also have scaly skin, which helps they be protected from abrasion and dehydration. Their circulatory system is closed with four chambers in their heart. Reptiles are cold-blooded, or <i>exothermic</i>, meaning that their blood temperature changes with their environment. This is helpful in saving energy for the reptile because they don't need to produce their own heat; instead they can lie in the sun. A fun fact is that snake charming actually doesn't hypnotize the snake with the music, but instead uses the movement of the performer to trip up the snake so it doesn't know when or where to strike. The reptile I have for you all today is the Freshwater Crocodile, or the <i>Crocodylus johnstoni</i>. This animal lives in freshwater lakes and wetlands, usually located in Australia and its lifespan is 30-40 years. The freshwater crocodile's diet can range from amphibians to even other reptiles or mammals.",
    #     "image": [
    #         "Images of Animals/Freshwater_crocodile.png"],
    #     "taxonomy":["Images of Animals/Reptiletax.png"] #Images of Reptiles
    #     ,
    #     "stylesheet":"Exhib8.css"
    # },
    # {
    #     "filename": "exhibit 9.html",
    #     "title": "Exhibit 9: Amphibians",
    #     "description": "Amphibians are really cool because they can breathe through both their lungs and their skin! Amphibian means '2 lives' in Greek. Unfortunately, amphibians aren't a phylum alone, and are part of the vertebrate phylum Chordata. Amphibians have bilateral symmetry with sexual reproduction that involves external fertilization. These oviparous creatures have a fascinating way of reproduction where the male will spread their sperm onto the eggs laid in the water by the female. But wait, amphibians are land animals, no? Well, as I have mentioned before, amphibian means '2 lives' in Greek. This means that they technically live two lives: one on land and one in the water. Amphibia are born in the water as eggs and then hatch into something like tadpoles. Then, the tadpoles start to lose their gills and grow lungs so that they can live on dry land. The amphibian that I'd like to show you all today is the American Bullfrog or the <i>Lithobates catesbeianus</i>. The American Bullfrog's habitat is obvious in America, near lakes or ponds. Their lifespan is 7–10 years. The American bullfrogs diet can consist of small bugs, insects, other amphibians, and really anything else it can find.",
    #     "image": [
    #         "Images of Animals/American_Bullfrog.png"],
    #     "taxonomy":["Images of Animals/Amphibiantax.png"] #Images of Amphibians
    #     ,
    #     "stylesheet":"Exhib9.css"
    # },
    # {
    #     "filename": "exhibit 10.html",
    #     "title": "Exhibit 10: Mammals",
    #     "description": "The next class is Mammals. Mammals have an closed circulatory system with bilateral symmetry, producing sexually through internal fertilizaiton. Mammals have warm blood and they feed their young with milk from teh mammary gland, unique amongst the other classes. The mammals I am showcasing here is the Siberian Tiger, known as the <i>Panthera tigris altaica</i>. Their habitat is usually forests in eastern Russia, Northeastern China, and North Korea and they live on average for only 10-15 years. The Siberian Tiger's diet consists of elk, boar, deer, water buffalo, and other similar animals.",
    #     "image": [
    #         "Images of Animals/Siberian_Tiger.png"],
    #     "taxonomy":["Images of Animals/Mammaltax.png"] #Images of Mammals
    #     ,
    #     "stylesheet":"Exhib10.css"
    # },
    # {
    #     "filename": "exhibit 11.html",
    #     "title": "Exhibit 11: Fish",
    #     "description": "The most confusing taxonomy, Pisces! So fish are actually a super-super-superclass (or just clade because they don't have a technical name) of the super-superclasses (or also clades) agnathans and gnathostomes (jawless vs jawed fish respectively), gnathostomes of which contain the superclasses chondrichthyes and osteichthyes, which are cartilaginous fish and bony fish respectively. But under those superclasses come the class of the fish that is shown above: actinopterygii. Actinopterygii are jawed bony fish who have ray fins, unlike sarcopterygii who have lobe fins. Fish have bilateral symmetry and sexually fertilize externally through eggs. Fish lay eggs, making them oviparous. Their circulatory system is closed with two chambers in their heart. They have a special way of gas exchange, called countercurrent, which uses gills to take out oxygen from the water and turn it into carbon dioxide. This above is the European Perch (Ahven), or <i>Perca fluviatilis</i>. Its habitat can just be any freshwater lake, usually in Europe and parts of Siberia. A European Perch's lifespan is around 7-10 years, reaching a maximum of 22. Their diet consists of zooplankton for juveniles and invertebrates as well as other fish like minnows for the mature.",
    #     "image": [
    #         "Images of Animals/European_perch.png"],
    #     "taxonomy":["Images of Animals/Fishtax.png"] #Images of Fish
    #     ,
    #     "stylesheet":"Exhib11.css"
    # }
#] 



#def generate_home_page():


def generate_index_page(exhibits: list[dict]) -> str:
    #Start Code for indexes
    links = "".join(
        f'      <li><a href="{ex["filename"]}">{ex["title"]}</a></li>\n' 
        for ex in exhibits
    )
  
   
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Start Exploring</title>
            <!-- Link to external CSS file-->
            <link rel="stylesheet" href="styles.css">
        </head>
        </html>

        <body>
            <h1>Welcome To The Haverinen Animal Education Website</h1>
            
            
            <img src="Images of Animals/ZOOMAP.png" usemap="#zoomap">
            <map name="zoomap">
                <area shape="rect" coords="40, 100, 120, 170" href="exhibit 1.html">
                <area shape="rect" coords="170, 100, 240, 170" href="exhibit 2.html">
                <area shape="rect" coords="250, 25, 330, 100" href="exhibit 3.html">
                <area shape="rect" coords="65, 190, 150, 270" href="exhibit 4.html">
                <area shape="rect" coords="45, 300, 130, 350" href="exhibit 5.html">
                <area shape="rect" coords="80, 365, 160, 440" href="exhibit 6.html">
                <area shape="rect" coords="200, 230, 270, 340" href="exhibit 7.html">
                <area shape="rect" coords="320, 325, 425, 425" href="exhibit 8.html">
                <area shape="rect" coords="320, 140, 390, 250" href="exhibit 9.html">
                <area shape="rect" coords="465, 215, 590, 305" href="exhibit 10.html">
                <area shape="rect" coords="490, 5, 590, 70" href="exhibit 11.html">
            </map>
            <p>Welcome to our interactive zoo interface of the HAEW. You can click anywhere on the map above to learn about animals. Or, you can go to the section below to see the exhibits if you don't feel like trying to find the correct place on the map. Once you think that you've learned enough, you can check your knowledge with a little quiz at the bottom of the page. You will thoroughly enjoy gazing at and learning about these eleven unique animals.</p>
            <section class="exhibits">
                <h2>Here is a list of exhibits</h2>
                
                {links}
                <br>
                <br>
                <br>
                <br>
                <a class="index-btn" href="Homepage.html">Back to Homepage</a>
                <a class="index-btn" href="Quiz_for_website.html">Check my knowledge</a>
        <body>
        <html>
    """
    
    


def generate_exhibit_page(exhibit, index, exhibits_count):
    #Write Code for Generating Exhibit Pages
    
    img_html = "".join(
        f'<img src="{src}" alt="{exhibit["title"]} image">' for src in exhibit["image"]
    )
    tax_html = "".join(
        f'<img src="{src}" alt="{exhibit["title"]} taxonomy">' for src  in exhibit["taxonomy"]
    )
    stylesheet_link = (
        f'<link rel = "stylesheet" href = "{exhibit["stylesheet"]}">' if exhibit["stylesheet"] else ""
    )


    #build previous/next navi
    nav_html = '<div style="margin-top: 20px;">\n'

    
    # If not the first exhibit, show previous link
    if index > 0:
        prev_filename = exhibits[index - 1]["filename"]
        nav_html += f"""      <a class="exhib-btn" href="{prev_filename}">Previous Exhibit</a>
        """
        
    #Veci Varse
    if index < exhibits_count - 1:
        next_filename = exhibits[index + 1]["filename"]
        nav_html += f"""      <a class="exhib-btn" href="{next_filename}">Next Exhibit</a>
        """

   
    nav_html += '</div>'

    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="Viewport" content="width=device-width, initial-scale=1.0">
    <title>{exhibit['title']}</title>
    {stylesheet_link}
</head>
<body>
    <div class="exhibits">
        <h1>{exhibit['title']}</h1>
        {img_html}
        <p>{exhibit['description']}</p>
        <br>
        {tax_html}
        {nav_html}
        
    </div class>
    <p></p>

    <a class="exhib-btn" href="index.html">Back to Main Page</a> <a class="exhib-btn" href="info.html">Definitions and Key Terms</a>

</body>
</html>
"""
    return html_content
    #Collapsed Code to Save Space

def main():
    global exhibits
    exhibits = csv_to_exhibits(csv_path)

    for i, exhibit in enumerate(exhibits):
        html = generate_exhibit_page(exhibit, i, len(exhibits))
        (output_dir / exhibit["filename"]).write_text(html, encoding="utf-8")

    (output_dir / "index.html").write_text(generate_index_page(exhibits))
    print(f"Site generate successfully in {output_dir}")
  
if __name__ == '__main__':
    main()

