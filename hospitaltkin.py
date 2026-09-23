import tkinter as tk
from tkinter import ttk, messagebox
import random

def generar_diagnostico():
    try:
        nombre = entry_nombre.get()
        if not nombre:
            messagebox.showwarning("Faltan datos", "Por favor ingresa el nombre del paciente.")
            return
            
        edad = int(entry_edad.get())
        peso = float(entry_peso.get().replace(',', '.'))
        

        talla = float(entry_talla.get().replace(',', '.'))
        if talla > 3.0: 
            talla = talla / 100.0
            
        presion_sis = int(entry_sis.get())
        presion_dia = int(entry_dia.get())
        
        P = var_fiebre.get()
        Q = var_tos.get()
        R = var_dolor.get()
        S = var_taqui.get()
        T = var_aire.get()

     
        if P and S and T:
            diag_sintomas = "EMERGENCIA: Infección sistémica o cardiopulmonar."
            consultorio = "Consultorio 1 (URGENCIAS)"
            receta = "Oxígeno suplementario, Antipiréticos IV."
            color_alerta = "#D32F2F" # Rojo emergencia
        elif P and Q and R:
            diag_sintomas = "Posible infección respiratoria aguda (Gripe/COVID)."
            consultorio = "Consultorio 2 (VÍAS RESPIRATORIAS)"
            receta = "Paracetamol 500mg c/8h, Jarabe, Reposo."
            color_alerta = "#F57C00" # Naranja
        elif S and T:
            diag_sintomas = "Cuadro de ansiedad aguda o arritmia."
            consultorio = "Consultorio 3 (CARDIOLOGÍA)"
            receta = "Electrocardiograma (ECG), Relajante muscular."
            color_alerta = "#F57C00"
        elif Q and R:
            diag_sintomas = "Irritación respiratoria o faringitis."
            consultorio = "Consultorio 4 (MEDICINA GENERAL)"
            receta = "Ibuprofeno 400mg c/8h, Líquidos."
            color_alerta = "#1976D2" # Azul normal
        elif P:
            diag_sintomas = "Cuadro febril sin patrón claro."
            consultorio = "Consultorio 4 (MEDICINA GENERAL)"
            receta = "Paracetamol 500mg. Observación 24 hrs."
            color_alerta = "#1976D2"
        else:
            diag_sintomas = "No se identificó un patrón grave."
            consultorio = "Consultorio 5 (ATENCIÓN PREVENTIVA)"
            receta = "Vitaminas, Buena hidratación."
            color_alerta = "#388E3C" # Verde sano

      
        alertas = []
        imc = peso / (talla ** 2)

        if imc < 18.5: alertas.append(f"Bajo peso (IMC: {imc:.1f})")
        elif 25 <= imc < 29.9: alertas.append(f"Sobrepeso (IMC: {imc:.1f})")
        elif imc >= 30: alertas.append(f"Obesidad (IMC: {imc:.1f})")

        if presion_sis > 140 or presion_dia > 90: alertas.append("Hipertensión detectada.")
        elif presion_sis < 90 or presion_dia < 60: alertas.append("Hipotensión detectada.")

        
        turno = random.randint(100, 999)
        minutos_espera = random.randint(5, 45)
        medico = random.choice(["Dr. Martínez", "Dra. Gómez", "Dr. Hernández", "Dra. Ramírez"])

        mostrar_ticket(nombre, edad, turno, minutos_espera, medico, consultorio, diag_sintomas, alertas, receta, color_alerta)

    except ValueError:
        messagebox.showerror("Error de Formato", "Asegúrate de ingresar solo números en Edad, Peso, Talla y Presión.")

def mostrar_ticket(nombre, edad, turno, espera, medico, consultorio, diag, alertas, receta, color_alerta):
    ventana = tk.Toplevel(root)
    ventana.title("Sistema Hospitalario - Ticket")
    ventana.geometry("400x550")
    ventana.configure(bg="#FFFFFF")
    ventana.resizable(False, False)


    frame_header = tk.Frame(ventana, bg=color_alerta, pady=15)
    frame_header.pack(fill="x")
    tk.Label(frame_header, text=f"TURNO: #{turno}", font=("Segoe UI", 20, "bold"), bg=color_alerta, fg="white").pack()
    tk.Label(frame_header, text=consultorio, font=("Segoe UI", 12), bg=color_alerta, fg="white").pack()

    # Cuerpo del ticket (Corrección aplicada en los anchor)
    frame_body = tk.Frame(ventana, bg="#FFFFFF", padx=25, pady=20)
    frame_body.pack(fill="both", expand=True)

    tk.Label(frame_body, text="DATOS DEL PACIENTE", font=("Segoe UI", 10, "bold"), bg="#FFFFFF", fg="#7F8C8D", anchor="w").pack(fill="x")
    tk.Label(frame_body, text=f"👤 {nombre} | {edad} años", font=("Segoe UI", 12), bg="#FFFFFF", fg="#2C3E50", anchor="w").pack(fill="x", pady=(0, 15))

    tk.Label(frame_body, text="DIAGNÓSTICO PRINCIPAL", font=("Segoe UI", 10, "bold"), bg="#FFFFFF", fg="#7F8C8D", anchor="w").pack(fill="x")
    tk.Label(frame_body, text=f"⚠️ {diag}", font=("Segoe UI", 11), bg="#FFFFFF", fg="#2C3E50", wraplength=350, justify="left", anchor="w").pack(fill="x", pady=(0, 15))

    tk.Label(frame_body, text="SIGNOS Y ALERTAS", font=("Segoe UI", 10, "bold"), bg="#FFFFFF", fg="#7F8C8D", anchor="w").pack(fill="x")
    texto_alertas = "\n".join([f"• {a}" for a in alertas]) if alertas else "• Signos vitales en rangos normales."
    tk.Label(frame_body, text=texto_alertas, font=("Segoe UI", 11), bg="#FFFFFF", fg="#2C3E50", justify="left", anchor="w").pack(fill="x", pady=(0, 15))

    tk.Label(frame_body, text="RECETA MÉDICA", font=("Segoe UI", 10, "bold"), bg="#FFFFFF", fg="#7F8C8D", anchor="w").pack(fill="x")
    tk.Label(frame_body, text=f"💊 {receta}", font=("Segoe UI", 11), bg="#FFFFFF", fg="#2C3E50", wraplength=350, justify="left", anchor="w").pack(fill="x", pady=(0, 15))

    # Pie del ticket
    frame_footer = tk.Frame(ventana, bg="#ECF0F1", pady=10)
    frame_footer.pack(fill="x", side="bottom")
    tk.Label(frame_footer, text=f"Atiende: {medico} | Espera: {espera} min", font=("Segoe UI", 10, "italic"), bg="#ECF0F1", fg="#34495E").pack()


root = tk.Tk()
root.title("Hanz Hospitalario Pro")
root.geometry("450x680")
root.resizable(False, False)


BG_APP = "#F4F6F9"
COLOR_PRIMARIO = "#005B96"
root.configure(bg=BG_APP)

style = ttk.Style()
style.theme_use("clam")


style.configure(".", background=BG_APP, font=("Segoe UI", 10))
style.configure("TLabelframe", background=BG_APP, bordercolor="#D5D8DC")
style.configure("TLabelframe.Label", font=("Segoe UI", 11, "bold"), foreground=COLOR_PRIMARIO, background=BG_APP)
style.configure("TCheckbutton", background=BG_APP, focuscolor="none")


style.configure("Action.TButton", font=("Segoe UI", 12, "bold"), background=COLOR_PRIMARIO, foreground="white", borderwidth=0, padding=10)
style.map("Action.TButton", background=[("active", "#003F6B")])

header = tk.Frame(root, bg=COLOR_PRIMARIO, pady=15)
header.pack(fill="x", pady=(0, 15))
tk.Label(header, text="⚕️ SISTEMA INTELIGENTE", font=("Segoe UI", 16, "bold"), bg=COLOR_PRIMARIO, fg="white").pack()

frame_datos = ttk.LabelFrame(root, text=" Información del Paciente ", padding=15)
frame_datos.pack(fill="x", padx=20, pady=5)

ttk.Label(frame_datos, text="Nombre:").grid(row=0, column=0, sticky="w", pady=4, padx=5)
entry_nombre = ttk.Entry(frame_datos, width=28)
entry_nombre.grid(row=0, column=1, columnspan=3, sticky="w", pady=4, padx=5)

ttk.Label(frame_datos, text="Edad (años):").grid(row=1, column=0, sticky="w", pady=4, padx=5)
entry_edad = ttk.Entry(frame_datos, width=28)
entry_edad.grid(row=1, column=1, columnspan=3, sticky="w", pady=4, padx=5)

ttk.Label(frame_datos, text="Peso (kg):").grid(row=2, column=0, sticky="w", pady=4, padx=5)
entry_peso = ttk.Entry(frame_datos, width=10)
entry_peso.grid(row=2, column=1, sticky="w", pady=4, padx=5)

ttk.Label(frame_datos, text="Estatura (m):").grid(row=2, column=2, sticky="w", pady=4, padx=5)
entry_talla = ttk.Entry(frame_datos, width=10)
entry_talla.grid(row=2, column=3, sticky="w", pady=4, padx=5)


frame_signos = ttk.LabelFrame(root, text=" Presión Arterial ", padding=15)
frame_signos.pack(fill="x", padx=20, pady=5)

ttk.Label(frame_signos, text="Sistólica:").grid(row=0, column=0, sticky="w", pady=4, padx=5)
entry_sis = ttk.Entry(frame_signos, width=10)
entry_sis.grid(row=0, column=1, sticky="w", pady=4, padx=5)

ttk.Label(frame_signos, text="Diastólica:").grid(row=0, column=2, sticky="w", pady=4, padx=15)
entry_dia = ttk.Entry(frame_signos, width=10)
entry_dia.grid(row=0, column=3, sticky="w", pady=4, padx=5)

frame_sintomas = ttk.LabelFrame(root, text=" Cuadro Clínico (Seleccionar) ", padding=15)
frame_sintomas.pack(fill="x", padx=20, pady=5)

var_fiebre = tk.BooleanVar()
var_tos = tk.BooleanVar()
var_dolor = tk.BooleanVar()
var_taqui = tk.BooleanVar()
var_aire = tk.BooleanVar()

ttk.Checkbutton(frame_sintomas, text="Fiebre (P)", variable=var_fiebre).grid(row=0, column=0, sticky="w", pady=2)
ttk.Checkbutton(frame_sintomas, text="Taquicardia (S)", variable=var_taqui).grid(row=0, column=1, sticky="w", padx=20, pady=2)
ttk.Checkbutton(frame_sintomas, text="Tos (Q)", variable=var_tos).grid(row=1, column=0, sticky="w", pady=2)
ttk.Checkbutton(frame_sintomas, text="Falta de aire (T)", variable=var_aire).grid(row=1, column=1, sticky="w", padx=20, pady=2)
ttk.Checkbutton(frame_sintomas, text="Dolor garganta (R)", variable=var_dolor).grid(row=2, column=0, sticky="w", pady=2)


btn_generar = ttk.Button(root, text="EMITIR DIAGNÓSTICO", style="Action.TButton", command=generar_diagnostico)
btn_generar.pack(pady=20, fill="x", padx=20)

root.mainloop()