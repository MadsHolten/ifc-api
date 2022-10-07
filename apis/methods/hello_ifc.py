import ifcopenshell, ifcopenshell.geom
from helpers import ld_tools

settings = ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS, True)
settings.set(settings.USE_PYTHON_OPENCASCADE, True)

async def extract(file_path):

    ifc_file = ifcopenshell.open(file_path)

    elements = ifc_file.by_type("IfcWindow")

    jsonld = {
        "@context": {
            "bot": "https://w3id.org/bot#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "ifc": "http://ifcowl.openbimstandards.org/IFC2X3_Final#"
        }
        ,"@graph": []}
    for element in elements:
        
        jsonld["@graph"].append({
            "@id": ld_tools.build_URI(element.GlobalId),
            "@type": ["bot:Element", "ifc:IfcWindow"],
            "rdfs:label": element.Name
        })

    return jsonld