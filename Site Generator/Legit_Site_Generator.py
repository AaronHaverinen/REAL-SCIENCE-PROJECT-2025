import os

#Set the optupt directory to your specified path
output_dir = r"/Users/aaronhaverinen/Documents/Science Project Folder 2025/Site Generator"

#Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    print("Directory doesn't exist; creating one now at", output_dir)
    os.makedirs(output_dir)
exhibits = [
    {
        "filename": "exhibit 1.html",
        "title": "Exhibit 1: Porifera",
        "description": "Our first animal phylum is called Porifera. Though it may not seem like it, sponges are actually animals and not plants. Porifera have neither organs nor true tissues but can produce both sexually and asexually through releasing sperm/eggs or budding, gemmules, and fragmentation. Additionally, Porifera are mostly assymetrical and sessile too. Here, I decided to showcase the Giant Barrel Sponge, also known as the <i>Xestospongia muta</i>. This animal lives mostly in the Gulf of America, near the Carribean Islands. Its diet consists of bacteria and plankton, as well as any other nutrition dissolved in the waters. The Giant Barrel Sponge, along with the whole phylum of Porifera, filter water through their pores and collect the food so that they can eat.",
        "image": [
            "Images of Animals/Giant_Barrel_Sponge.png" #Images of Porifera
        ],
        "stylesheet": "Exhib1.css"
    },
    {
        "filename": "exhibit 2.html",
        "title": "Exhibit 2: Cnidaria",
        "description": "Our next phylum is named Cnidaria. Cnidaria can range from corals to jellyfish. This is the only phylum that has both medusa and polyp stages, meaning that it can start from looking like a plant into the ocean, and then grow into something that looks like a fish. Cnidaria are symmetrical, producing both sexually and asexually like Porifera. This is also the only phylum that uses tentacles to sting and catch prey. Here, I decided to display the Lion's Mane Jellyfish, also known as the <i>Cyanea capillata</i>. The Lions Mane Jellyfish lives in the Arctic, North Atlantic, and North Pacific Oceans, eating zooplankton, small fish, and even other jellyfish! The tentacles of this jellyfish can get as long as a hundred feet and its bell is around 8 feet in diameter. That's huge!",
        "image": [
            "Images of Animals/Lions_Mane_Jellyfish.png" #Images of Cnidaria
        ],
        "stylesheet": "Exhib2.css"
    },
    {
        "filename": "exhibit 3.html",
        "title": "Exhibit 3: Mollusca",
        "description": "These are Mollusca, also known as Mollusks. Mollusca can have multiple hearts in their open circulatory system. This phylum differs from Porifera and Cnidaria because it actually has blood to circulate. Mollusca have bilateral symmetry, producing sexually through external fertilization. Some Mollusca have shells while others do not. Here I am showcasing the Giant Pacific Octopus, known taxonomically as the <i>Enteroctopus dofleini</i>. This is a type of Mollusca that does not have a shell, like squids. However, all mollusca do have a mantel for protection. The Giant Pacific Octopus lives only about 3-5 years in the Pacific Ocean (as described in the name). Its diet can include shrimp, crab, scallops, lobster, and other seafood of that type. As a fun fact, this octopus has nine brains! It has one central one and one for each arm. How lucky.",
        "image": [
            "Images of Animals/Giant_Pacific_Octopus.png" #Images of Mollusca
        ]
    },
    {
        "filename": "exhibit 4.html",
        "title": "Exhibit 4: Annelida",
        "description": "The next phylum is Annelida. These animals have bilateral symmetry and you might also know these as worms. The most notable of these are actually earthworms. Annelida reproduce sexually, though they are both genders at once. They have a closed circulatory system with no heart. Instead, they have bloods through capilaries in their body. Their digestive system is complete, running from mouth to anus. And even though they have no eyes, annelida can still sense the presence of light. Today, I am using the Red Tiger Worm, the <i>Eisenia Andrei</i>, as our example. This earthworm lives around 5 years in usually compost or dung heaps. The diet of this animal is really just any type of decomposing matter, usually produce.",
        "image": [
            "Images of Animals/Red_Earthworm.png" #Images of Annelida
        ],
        "name_of_animal": "The Red Tiger Worm"
    },
    {
        "filename": "exhibit 5.html",
        "title": "Exhibit 5: Arthropoda",
        "description": "Arthropoda is one of the biggest phylum, including many animals like insects, crustaceans, etc. This phylum also has bilateral symmetry with an open circulatory system with hemolymph, a liquid similar to blood. Arthropoda reproduce sexually and have two different types of metamorphosis: complete and incomplete. The complete metamorphosis has four stages with a larva and pupa while incomplete has three with a nymph. The animal I am showcasing for this phylum is the American Lobster, known as the <i>Homarus americanus</i>. The American Lobster lives for around 100 years in the cold wwaters of the northwest pacific in the eastcoast of the United States. Its diet can range from mollusks to worms to urchins and more. Fun fact: when you cook lobsters, they become red!",
        "image": [
            "Images of Animals/American_Lobster.png" #Images of Arthropods
        ]
    },
    {
        "filename": "exhibit 6.html",
        "title": "Exhibit 6: Echinodermata",
        "description": "This phylum is the last invertibrate one before we move onto vertebrates. You may have seen these wash up on the beach and think these are just cool rocks or dead plants, but these are actually animals. Echinodermata can include starfish, sand dollars, and even sea urchins. Echinodermata have bilateral symmetry when they are immature but grow into radial (or pentaradial) symmetry when fully grown. Echinodermata reproduce mainly via sexual reproduction but can also exhibit assexual reproduction through fragmentation. The echinodermatum that I have decided to show you all is the Common Starfish, or <i>Asterias rubens</i>. These Starfish live in the waters of the Atlantic Ocean for around 5 to 10 years. Their diet is carnivorous, hosting mollusks like clams, mussels, and barnacles.",
        "image": [
            "Images of Animals/Starfish.png" #Images of Echinodermata
        ]
    },
    {
        "filename": "exhibit 7.html",
        "title": "Exhibit 7: Aves",
        "description": "This next phylum will be chordata, with our last five animals being classes of that phylum. The first class is Aves. Aves are the first class that I will show you of vertebrates. Aves have an closed circulatory system with bilateral symmetry, producing sexually through internal fertilizaiton. Aves have wings and are really the only phylum that can fly. The bird I am showcasing here is the Blue Jay, known as the <i>Cyanocitta cristata</i>. Their habitat is usually mised woodlnads in Northeastern America and their lifespan is around 7 years. The blue jay's diet consists of seeds, nuts, and insects.",
        "image": [
            "Images of Animals/Blue_Jay.png" #Images of Aves
        ]
    },
    {
        "filename": "exhibit 8.html",
        "title": "Exhibit 8: Reptiles",
        "description": "Our next class of chordata will be Reptiles. This is a cold-blooded (meaning their blood temperature changes with the environment) type of vertebrate which usually has scaly skin. Reptiles have closed circulatory systems with one heart. Reptiles have bilateral symmetry, producing sexually through internal fertilization. The reptile here today is the Freshwater Crocodile, or <i>Crocodylus johnstoni</i>. This animal lives in freshwater lakes and wetlands usually located in Australia. Their lifespan is 30 to 40 years. The freshwater crocodile's diet can be amphibians, reptiles, small mammals, and even other reptiles.",
        "image": [
            "Images of Animals/Freshwater_crocodile.png" #Images of Reptiles
        ]
    },
    {
        "filename": "exhibit 9.html",
        "title": "Exhibit 9: Amphibians",
        "description": "The next class is Amphibian. Amphibians have an closed circulatory system with bilateral symmetry, producing sexually through external fertilizaiton. Amphibians usually start off in the water, but then gradually go to living on land. The amphibian I am showcasing here is the American Bullfrog, known as the <i>Lythobates catesbeianus</i>. Their habitat is usually lakes, ponds, or marshes and they live for around 7-10 years. The American Bullfrog's diet consists of insects, grasshoppers, beetles, spiders, etc.",
        "image": [
            "Images of Animals/American_Bullfrog.png" #Images of Amphibians
        ]
    },
    {
        "filename": "exhibit 10.html",
        "title": "Exhibit 10: Mammals",
        "description": "The next class is Mammals. Mammals have an closed circulatory system with bilateral symmetry, producing sexually through internal fertilizaiton. Mammals have warm blood and they feed their young with milk from teh mammary gland, unique amongst the other classes. The mammals I am showcasing here is the Siberian Tiger, known as the <i>Panthera tigris altaica</i>. Their habitat is usually forests in eastern Russia, Northeastern China, and North Korea and they live on average for only 10-15 years. The Siberian Tiger's diet consists of elk, boar, deer, water buffalo, and other similar animals.",
        "image": [
            "Images of Animals/Siberian_Tiger.png" #Images of Mammals
        ]
    },
    {
        "filename": "exhibit 11.html",
        "title": "Exhibit 11: Fish",
        "description": "The last class is Fish or more specifically, Actinopterygii. Fish have an closed circulatory system (cold-blodded) with bilateral symmetry, producing sexually through external fertilizaiton. Fish breathe through countercurrent exchange where they use gills to exchange oxygen in the water for carbon dioxide. There are many types and classes of fish, for example jawless, (jawed) bony or cartilaginous. The Actinopterygii is a type of bony fish, which has ray fins, unlike Sarcopterygii who have lobe fins. The fish I am showcasing here is the European Perch, known as the <i>Perca fluviatilis</i>. Their habitat is really any freshwater source like lakes and they live primarily in Europe and parts of Siberia. A European Perch's lifespan is around 7-10 years, reaching a maximum of 22. Their diet consists of zooplankton for juveniles and invertibrates as well as other fish like minnows for the mature.",
        "image": [
            "Images of Animals/European_perch.png" #Images of Fish
        ]
    }
] 



def generate_index_page(exhibits):
    #Start Code
    exhibit_links = ""
    for exhibit in exhibits:
        exhibit_links += f'         <li><a href="{exhibit["filename"]}">{exhibit["title"]}</a></li>\n'
    html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Exhibit Page</title>
            <!-- Link to external CSS file-->
            <link rel="stylesheet" href="styles.css">
        </head>
        </html>

        <body>
            <h1>Welcome To The Animal Captivity Place </h1>
            
            
            <img src="Images of Animals/MAYBEZOOMAP.png" usemap="#zoomap">
            <map name="zoomap">
                <area shape="rect" coords="35, 250, 80, 320" href="exhibit 1.html">
                <area shape="rect" coords="82, 250, 127, 320" href="exhibit 2.html">
                <area shape="rect" coords="130, 250, 175, 320" href="exhibit 3.html">
                <area shape="rect" coords="50, 20, 150, 90" href="exhibit 4.html">
                <area shape="rect" coords="220, 270, 310, 365" href="exhibit 5.html">
                <area shape="rect" coords="310, 270, 400, 365" href="exhibit 6.html">
                <area shape="rect" coords="220, 70, 340, 170" href="exhibit 7.html">
                <area shape="rect" coords="370, 140, 420, 220" href="exhibit 8.html">
                <area shape="rect" coords="420, 140, 470, 220" href="exhibit 9.html">
                <area shape="rect" coords="470, 10, 560, 80" href="exhibit 10.html">
                <area shape="rect" coords="630, 80, 700, 130" href="exhibit 11.html">
            </map>
            <p>Here at the ACP, we hold animals in captive, 11 to be exact, and you can see them all here. Just follow the map and GO IN ORDER so that you do miss out on valuable information. Click on the correct places on the map above to direct you to different exhibits. Or, you can see the section below if you don't feel like, you know, going <i>treasure hunting</i>.</p>
            <section class="exhibits">
                <h2>Here is a list of exhibits</h2>
                
                {exhibit_links}
        <body>
        <html>
    """
    #WE NEED TO DO MAP LINE 120
    return html_content


def generate_exhibit_page(exhibit):
    print("Entering Exhibit Page Creation")
    image_html = ""
    if "image" in exhibit and exhibit["image"]:
        for img_path in exhibit["image"]:
            image_html += f'<img src="{img_path}" alt="{exhibit["title"]} image">'
    styleSheet = ""
    if "stylesheet" in exhibit and exhibit["stylesheet"]:
        for style_path in exhibit["stylesheet"]:
            styleSheet += f'<link rel="stylesheet" href="{style_path}">'
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="Viewport" content="width=device-width, initial-scale=1.0">
    <title>{exhibit['title']}</title>
    {styleSheet}
</head>
<body>
    <div class="exhibits">
        <h1>{exhibit['title']}</h1>
        {image_html}
        <p>{exhibit['description']}</p>
        <a href="index.html">Back to First Page</a>
    </div class>
</body>
</html>
"""
    return html_content

def main():
    
    print("Site Generator Process: Webstite srating")
    for exhibit in exhibits:
        content = generate_exhibit_page(exhibit)
        file_path = os.path.join(output_dir, exhibit["filename"])
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    generate_index_page(exhibits)
    index_content = generate_index_page(exhibits)
    print (index_content)
    index_path = os.path.join(output_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as stream:
        stream.write(index_content)
    print("Site generated successfully in", output_dir)

if __name__ == '__main__':
    main()

