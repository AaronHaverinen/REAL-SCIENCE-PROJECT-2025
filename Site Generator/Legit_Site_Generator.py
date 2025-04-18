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
        "description": "Though it may not seem as such, sea sponges are actually animals, and not plants. Sailors used to collect them to make dishwashing equipment (what now is synthetic). Now, porifera are mostly asymmetrical, reproducing both sexually and asexually. But this seems a bit strange. How can an animal reproduce both sexually and asexually? Well actually, asexual reproduction with porifera (or sponges) works via fragmentation, budding, or gemmules. Sexual reproduction occurs through releasing sperm or egg cells, where they float through the water to find another sponge, fertilizing it. However, sponges don't have true tissues or organs and are sessile, meaning not moving. Some fun facts about porifera are that they are filter-feeders, meaning that they filter water through themselves to extract the solids dissolved (i.e. plankton). This beauty above is the Giant Barrel Sponge, also known scientifically (or by its fancy name), <i>Xestospongia muta</i>. Their habitat is along the Caribbean and Gulf of America, most commonly on coral reefs. The Giant Barrel Sponge has a really long life span of around 2000 years! That means some sponges that are still living in our ocean today may have been alive when Jesus was doing his ministry! The Giant Barrel Sponge feeds on bacteria, plankton, prochlorophytes, and really any other nutrition dissolved in the water. It is not that picky. Another fun fact about sponges is that they are called porifera because of their many pores. Below is the taxonomy.",
        "image": [
            "Images of Animals/Giant_Barrel_Sponge.png", #Images of Porifera
        ],
        "taxonomy": ["Images of Animals/Poriferatax.png"],
        "stylesheet": "Exhib1.css"
    }, 
    {
        "filename": "exhibit 2.html",
        "title": "Exhibit 2: Cnidaria",
        "description": "Cnidaria is just a fancy Latin word for this phylum, which includes jellyfish, corals, and many others. Cnidaria are unique because they are the only phylum that has both the medusa and polyp stages. If you do not know what this means, it is completely OK. A jellyfish will start from an egg, then grow into a polyp, attached to the ground and commonly mistaken as a plant or even sponge, and then finally grow into a medusa with its large bell and tentacles. Cnidaria, like sponges, produce both sexually and asexually too. The asexual way works with budding, where the cnidarian can break off a bit of its body and then grow a new cnidarian out of it. Sexual reproduction works similarly to other animals by releasing sperm to fertilize females. Cnidaria also have tentacles, whose purpose is to sting and catch prey. This serves as an advantage to being a predator in the ocean. A funny fact about cnidaria is that they look like mushrooms. The cnidarian I've decided to showcase today is the Lion's Mane Jellyfish, also known by its boring name, the <i>Cyanea capillata</i>. This humongous jellyfish can grow tentacles as long as a hundred feet and its bell's circumference up to thirty feet! It lives in the cold waters of the Arctic, North Atlantic, and North Pacific Oceans. However, this glorious jellyfish only lives about twelve months, which is nothing compared to some other sea creatures. Its diet consists of zooplankton, small fish, and maybe even some other jellyfish occasionally. Below is the taxonomy.",
        "image": [
            "Images of Animals/Lions_Mane_Jellyfish.png"
        ],
        "taxonomy":["Images of Animals/Cnidariatax.png"], #Images of Cnidaria
    
        "stylesheet": "Exhib2.css"
    },
    {
        "filename": "exhibit 3.html",
        "title": "Exhibit 3: Mollusca",
        "description": "These are mollusca, a phylum that you're probably a bit familiar with. Their symmetry pattern is bilateral. Mollusca differ from other phyla because they actually have multiple hearts in their open circulatory system. Mollusca reproduce sexually through external fertilization, unlike most animals who reproduce internally. Some mollusks have shells and some do not, but all of them do have a mantle for protection. Above, I am showcasing the Giant Pacific Octopus, also known scientifically as the <i>Enteroctopus dofleini</i>. Their lifespan is around 3–5 years in the Pacific Ocean. Also, the Giant Pacific Octopus' diet can range from shrimp and crab to lobster and even more. As some fun facts, octopuses in general can change their color to camouflage with surroundings and can squirt ink to get away from enemies. And also, this specific octopus has nine brains! It has one central one for control and dominion over the other eight, which control each arm. How lucky. Imagine how much more innovation there would be if we each had nine brains! I'm just joking. Below is the taxonomy.",
        "image": [
            "Images of Animals/Giant_Pacific_Octopus.png"
        ],
        "taxonomy": ["Images of Animals/Molluscatax.png"], #Images of Mollusca
        
        "stylesheet": "Exhib3.css"
    },
    {
        "filename": "exhibit 4.html",
        "title": "Exhibit 4: Annelida",
        "description": "Now this phylum has a weird name (not saying that the others don't but yeah), annelida. There's nothing really too <i>special</i> about them, though they can see light without even any eyes and they breathe through a moist layer of water on their skin. That's why you can see that earthworms die when dried in the sun for a while. Annelids have bilateral symmetry and reproduce sexually, even though they are both genders at once! They rub against each other and exchange DNA to keep the line going. Their circulatory system is closed with some sort of heart-like structure. Their digestive system is complete, running all the way from their mouth to anus. Now this annelid that I have decided to show all of you today is the Red Tiger Worm, the <i>Eisenia andrei</i> (named by some scientists). This worm lives for around 5 years, usually residing in composts or dung heaps, or sometimes underground. It eats basically any decomposing matter it can find, usually some sort of produce. There really isn't much else to say. Below is the taxonomy.",
        "image": [
            "Images of Animals/Red_Earthworm.png"],
        "taxonomy": ["Images of Animals/Annelidatax.png"], #Images of Annelida
        
        
        "stylesheet": "Exhib4.css"
    },
    {
        "filename": "exhibit 5.html",
        "title": "Exhibit 5: Arthropoda",
        "description": "",
        "image": [
            "Images of Animals/American_Lobster.png"],
        "taxonomy": ["Images of Animals/Arthropodatax.png"] #Images of Arthropods
        ,
        "stylesheet": "Exhib5.css"
    },
    {
        "filename": "exhibit 6.html",
        "title": "Exhibit 6: Echinodermata",
        "description": "This phylum is the last invertibrate one before we move onto vertebrates. You may have seen these wash up on the beach and think these are just cool rocks or dead plants, but these are actually animals. Echinodermata can include starfish, sand dollars, and even sea urchins. Echinodermata have bilateral symmetry when they are immature but grow into radial (or pentaradial) symmetry when fully grown. Echinodermata reproduce mainly via sexual reproduction but can also exhibit assexual reproduction through fragmentation. The echinodermatum that I have decided to show you all is the Common Starfish, or <i>Asterias rubens</i>. These Starfish live in the waters of the Atlantic Ocean for around 5 to 10 years. Their diet is carnivorous, hosting mollusks like clams, mussels, and barnacles.",
        "image": [
            "Images of Animals/Starfish.png"],
        "taxonomy":["Images of Animals/Echinotax.png"] #Images of Echinodermata
        ,
        "stylesheet": "Exhib6.css"
    },
    {
        "filename": "exhibit 7.html",
        "title": "Exhibit 7: Aves",
        "description": "This next phylum will be chordata, with our last five animals being classes of that phylum. The first class is Aves. Aves are the first class that I will show you of vertebrates. Aves have an closed circulatory system with bilateral symmetry, producing sexually through internal fertilizaiton. Aves have wings and are really the only phylum that can fly. The bird I am showcasing here is the Blue Jay, known as the <i>Cyanocitta cristata</i>. Their habitat is usually mixed woodlands in Northeastern America and their lifespan is around 7 years. The blue jay's diet consists of seeds, nuts, and insects.",
        "image": [
            "Images of Animals/Blue_Jay.png"],
        "taxonomy":["Images of Animals/Avestax.png"] #Images of Aves
        ,
        "stylesheet": "Exhib7.css"
    },
    {
        "filename": "exhibit 8.html",
        "title": "Exhibit 8: Reptiles",
        "description": "Our next class of chordata will be Reptiles. This is a cold-blooded (meaning their blood temperature changes with the environment) type of vertebrate which usually has scaly skin. Reptiles have closed circulatory systems with one heart. Reptiles have bilateral symmetry, producing sexually through internal fertilization. The reptile here today is the Freshwater Crocodile, or <i>Crocodylus johnstoni</i>. This animal lives in freshwater lakes and wetlands usually located in Australia. Their lifespan is 30 to 40 years. The freshwater crocodile's diet can be amphibians, reptiles, small mammals, and even other reptiles.",
        "image": [
            "Images of Animals/Freshwater_crocodile.png"],
        "taxonomy":["Images of Animals/Reptiletax.png"] #Images of Reptiles
        ,
        "stylesheet":"Exhib8.css"
    },
    {
        "filename": "exhibit 9.html",
        "title": "Exhibit 9: Amphibians",
        "description": "The next class is Amphibian. Amphibians have an closed circulatory system with bilateral symmetry, producing sexually through external fertilizaiton. Amphibians usually start off in the water, but then gradually go to living on land. The amphibian I am showcasing here is the American Bullfrog, known as the <i>Lythobates catesbeianus</i>. Their habitat is usually lakes, ponds, or marshes and they live for around 7-10 years. The American Bullfrog's diet consists of insects, grasshoppers, beetles, spiders, etc.",
        "image": [
            "Images of Animals/American_Bullfrog.png"],
        "taxonomy":["Images of Animals/Amphibiantax.png"] #Images of Amphibians
        ,
        "stylesheet":"Exhib9.css"
    },
    {
        "filename": "exhibit 10.html",
        "title": "Exhibit 10: Mammals",
        "description": "The next class is Mammals. Mammals have an closed circulatory system with bilateral symmetry, producing sexually through internal fertilizaiton. Mammals have warm blood and they feed their young with milk from teh mammary gland, unique amongst the other classes. The mammals I am showcasing here is the Siberian Tiger, known as the <i>Panthera tigris altaica</i>. Their habitat is usually forests in eastern Russia, Northeastern China, and North Korea and they live on average for only 10-15 years. The Siberian Tiger's diet consists of elk, boar, deer, water buffalo, and other similar animals.",
        "image": [
            "Images of Animals/Siberian_Tiger.png"],
        "taxonomy":["Images of Animals/Mammaltax.png"] #Images of Mammals
        ,
        "stylesheet":"Exhib10.css"
    },
    {
        "filename": "exhibit 11.html",
        "title": "Exhibit 11: Fish",
        "description": "The last class is Fish or more specifically, Actinopterygii. Jawed fish are categorized into two superclasses: Chondrichtyes and Osteichthyes, the first one being cartilaginous and the latter being bony. The Actinopterygii is a type of bony fish, which has ray fins, unlike Sarcopterygii who have lobe fins. Fish have an closed circulatory system (cold-blodded) with bilateral symmetry, producing sexually through external fertilizaiton. Fish breathe through countercurrent exchange where they use gills to exchange oxygen in the water for carbon dioxide. The fish I am showcasing here is the European Perch, known as the <i>Perca fluviatilis</i>. Their habitat is really any freshwater source like lakes and they live primarily in Europe and parts of Siberia. A European Perch's lifespan is around 7-10 years, reaching a maximum of 22. Their diet consists of zooplankton for juveniles and invertibrates as well as other fish like minnows for the mature.",
        "image": [
            "Images of Animals/European_perch.png"],
        "taxonomy":["Images of Animals/Fishtax.png"] #Images of Fish
        ,
        "stylesheet":"Exhib11.css"
    }
] 



#def generate_home_page():


def generate_index_page(exhibits):
    #Start Code for indexes
    exhibit_links = ""
    for exhibit in exhibits:
        exhibit_links += f'         <li><a href="{exhibit["filename"]}">{exhibit["title"]}</a></li>\n'
    html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Start Exploring</title>
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
    
    return html_content


def generate_exhibit_page(exhibit, index, exhibits_count):
    #Write Code for Generating Exhibit Pages
    print("Entering Exhibit Page Creation")
    image_html = ""
    if "image" in exhibit and exhibit["image"]:
        for img_path in exhibit["image"]:
            image_html += f'<img src="{img_path}" alt="{exhibit["title"]} image">'
    styleSheet = ""
    if "stylesheet" in exhibit and exhibit["stylesheet"]:
        styleSheet += f'<link rel="stylesheet" href="{exhibit["stylesheet"]}">'
    tax_html = ""
    if "taxonomy" in exhibit and exhibit["taxonomy"]:
        for tax_path in exhibit["taxonomy"]:
            tax_html += f'<img src="{tax_path}" alt="{exhibit["title"]} taxonomy">'

    #build previous/next navi
    nav_html = '<div style="margin-top: 20px;">\n'

    
    # If not the first exhibit, show previous link
    if index > 0:
        prev_filename = exhibits[index - 1]["filename"]
        nav_html += f'      <a href="{prev_filename}" style="Margin-right: 20 px;<">Previous Exhibit'
        
    #Veci Varse
    if index < exhibits_count - 1:
        next_filename = exhibits[index + 1]["filename"]
        nav_html += f"""    <button class="btn-1" href="{next_filename}"><span>Next Exhibit</span></button>
        <link rel="stylesheet" href="Nxt_Exhib_Btn.css">
        """

   
    nav_html += '</div>'

    
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
        <br>
        {tax_html}
        {nav_html}
       
        <a href="index.html">Back to First Page</a>
        
    </div class>
</body>
</html>
"""
    return html_content

def main():
    
    print("Site Generator Process: Webstite srating")
    i = 0
    exhibits_count = len(exhibits)
    for exhibit in exhibits:
        content = generate_exhibit_page(exhibit, i, exhibits_count)
        file_path = os.path.join(output_dir, exhibit["filename"])
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        i+=1
    generate_index_page(exhibits)
    index_content = generate_index_page(exhibits)
    print (index_content)
    index_path = os.path.join(output_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as stream:
        stream.write(index_content)
    print("Site generated successfully in", output_dir)

if __name__ == '__main__':
    main()

