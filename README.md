# CryptoPass Generator
<img width="1863" height="522" alt="image" src="https://github.com/user-attachments/assets/acf3c49e-b69b-48bb-bbee-f6363f0fc3eb" />

Una aplicación web ligera y segura desarrollada en **Flask** que genera contraseñas robustas. A diferencia de los generadores tradicionales que crean caracteres aleatorios que el usuario debe almacenar, este sistema actúa como un generador criptográfico: utiliza una clave maestra, el nombre del servicio y un número semilla pseudoaleatorio para calcular siempre la misma contraseña segura de manera matemática, eliminando la necesidad de guardar datos sensibles en servidores.

## 🚀 Características Principales
* **Generación Determinista:** Produce siempre la misma clave robusta si los datos de entrada coinciden, actuando como un sistema "sin almacenamiento" (Zero-Storage).
* **Entropía Criptográfica:** Integra el nombre del servicio (ej. Netflix, Gmail), una contraseña común del usuario y una **semilla numérica** para maximizar la complejidad criptográfica.
* **Seguridad por Diseño:** El sistema funciona bajo el principio de un hash personalizado; no guarda registros de las contraseñas ni de las semillas en bases de datos, garantizando la privacidad absoluta.
* **Interfaz Limpia:** Formulario web intuitivo con retroalimentación inmediata para copiar la contraseña generada con un solo clic.

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python 3.x, Flask Framework
* **Criptografía / Lógica:** Módulos nativos de Python (`hashlib`, `random` con inicialización de semilla)
* **Frontend:** HTML5, CSS3 (Diseño Responsivo), JavaScript
* **Control de Versiones:** Git & GitHub

## 📐 Cómo funciona la lógica interna
El núcleo de la aplicación utiliza el **número semilla** y la contraseña original para inicializar el estado del generador pseudoaleatorio o crear un hash combinado (HMAC/SHA-256). Al combinar estos tres factores (Clave + Aplicación + Semilla), se garantiza que:
1. Contraseñas comunes se transformen en hashes de alta seguridad con caracteres especiales, mayúsculas y números.
2. Nadie pueda replicar la contraseña sin conocer exactamente la semilla numérica utilizada como factor de autenticación adicional.

## 💻 Instalación y Uso Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   cd generador-contrasenas-flask
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python app/main.py 
   ```
   Abre [http://127.0.0.1:5000](http://127.0.0.1:5000) en tu navegador.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT.
