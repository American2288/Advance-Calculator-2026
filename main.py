import flet as ft

def main(page: ft.Page):
    page.title = "Mera Flet Calculator"
    page.bgcolor = "#000000"  # Dark Theme
    
    # Ek simple button check karne ke liye
    btn = ft.ElevatedButton(text="Click Karke Dekho!", color="white", bgcolor="blue")
    
    page.add(btn)

ft.app(target=main)
