import streamlit as st
import datetime

# Configuration de la page
st.set_page_config(page_title="Récupération KBIS - AJA", page_icon="📄")

st.title("📄 Demande de KBIS & Information")
st.write("Veuillez remplir le formulaire ci-dessous pour accéder au document.")

# --- FORMULAIRE UTILISATEUR ---
with st.form("demande_kbis"):
    col1, col2 = st.columns(2)
    
    with col1:
        nom = st.text_input("Nom")
    with col2:
        prenom = st.text_input("Prénom")
        
    objet = st.text_area("Objet de l'utilisation du KBIS", 
                         placeholder="Ex: Ouverture de compte, dossier de subvention...")
    
    submit_button = st.form_submit_button("Valider la demande")

# --- LOGIQUE APRÈS VALIDATION ---
if submit_button:
    if not nom or not prenom or not objet:
        st.error("Veuillez remplir tous les champs avant de continuer.")
    else:
        st.success(f"Merci {prenom} {nom}. Votre demande a été enregistrée.")
        
        # 1. Section Mail d'information
        st.subheader("✉️ Mail d'information généré")
        destinataire = "wiki-aja@ajassocies.fr"
        sujet = f"Demande de KBIS - {nom} {prenom}"
        corps_mail = f"""
        Bonjour,
        
        L'utilisateur {prenom} {nom} a généré une demande de KBIS le {datetime.date.today()}.
        Objet de l'utilisation : {objet}
        
        Cordialement,
        Système Automatisé AJA
        """
        
        st.info(f"**Destinataire :** {destinataire}")
        st.code(f"Sujet : {sujet}\n\n{corps_mail}", language="text")
        
        # Bouton factice pour copier/envoyer le mail
        st.link_button("Envoyer le mail (via votre messagerie)", 
                       f"mailto:{destinataire}?subject={sujet}&body={corps_mail}")

        st.divider()

        # 2. Section Téléchargement du KBIS
        st.subheader("📥 Téléchargement du document")
        
        # Note : Remplacez 'kbis_exemple.pdf' par le chemin réel de votre fichier
        # Pour le test, nous créons un bouton qui simule le téléchargement
        try:
            with open("kbis_aja.pdf", "rb") as file:
                st.download_button(
                    label="Télécharger le KBIS (PDF)",
                    data=file,
                    file_name=f"KBIS_AJA_{nom}.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.warning("Fichier KBIS source introuvable. Veuillez placer un fichier nommé 'kbis_aja.pdf' dans le dossier du script.")
