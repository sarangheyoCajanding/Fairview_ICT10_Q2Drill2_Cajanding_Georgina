from pyscript import document

grade_7 = {"Mateo Salacup", "Maggie Chiong"}
grade_8 = {"Sam Bautista", "Cianna Del Prado"}
grade_9 = {"Chloe Adlawan", "Inno Pena"}
grade_10 = {"Erin Rioflorido", "Julia Bermudez"}

new_members = set()

def add_member(event):
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value

    name = first + " " + last

    new_members.add(name)
    members = grade_7 | grade_8 | grade_9 | grade_10 | new_members

    document.getElementById("results").innerHTML = f"""
    <h4>Dance Club Members</h4>
    <p>{", ".join(sorted(members))}</p>
    <h5>Total Members: {len(members)}</h5>
    """

    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""
