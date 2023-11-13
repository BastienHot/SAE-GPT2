import gradio as gr

def ecrire_dans_fichier(texte):
    nom_fichier = "sortie.txt"
    with open(nom_fichier, "w") as fichier:
        fichier.write(texte)
    return f"Contenu enregistré dans {nom_fichier}"

iface = gr.Interface(
    fn=ecrire_dans_fichier,
    inputs=gr.Textbox(),
    outputs="text",
    live=True,
    title="Gradio - Écrire dans un fichier",
    description="Saisissez du texte et appuyez sur le bouton pour l'enregistrer dans un fichier texte.",
    theme="default",
    allow_flagging=False,
)

iface.launch()