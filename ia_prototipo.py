import os
import pandas as pd
from dotenv import load_dotenv
# Importamos el módulo 'openai' para la comunicación con la API.
from openai import OpenAI

# -----------------------------------------------------------
# 1. Configuración de la API Key (Seguridad)
# -----------------------------------------------------------
# Carga las variables de entorno desde el archivo .env
load_dotenv()
# Intentamos obtener la clave. Si no existe, se cargará como None.
api_key = os.getenv("OPENAI_API_KEY")

# Inicializa el cliente de OpenAI. Esto fallará si la clave es inválida, 
# pero lo manejamos en la función de generación con el modo simulación.
client = None
if api_key and api_key != 'TU_CLAVE_AQUI':
    try:
        client = OpenAI(api_key=api_key)
    except Exception as e:
        print(f"Advertencia: Error al inicializar el cliente OpenAI: {e}")
        print("Continuando en modo simulación...")

# -----------------------------------------------------------
# 2. Función de Generación de Biografía (El Prototipo IA 3 con SIMULACIÓN)
# -----------------------------------------------------------
def generar_bio_ia(datos_animal):
    """
    Simula la llamada a GPT-3 para generar una biografía emocional 
    basada en los datos estructurados del animal.
    
    Args:
        datos_animal (str): Cadena de texto con los datos clave del animal.
        
    Returns:
        str: La biografía generada (real o simulada).
    """
    # Parseamos los datos clave de la entrada para usarlos en la simulación
    datos_partes = datos_animal.split(';')
    nombre = datos_partes[0]
    raza = datos_partes[1]
    edad = datos_partes[2]
    condicion = datos_partes[3]
    
    # *** Lógica de Simulación (para evitar el AuthenticationError) ***
    # Si la clave no es válida o es el placeholder, usamos la simulación
    if api_key == 'TU_CLAVE_AQUI' or not client:
        print(f"\nSIMULACIÓN: Generando Bio Local para {nombre}...")
        return (
            f"SIMULACIÓN: {nombre} ({edad} años) es un/a encantador/a {raza} "
            f"con una Condición Especial: **{condicion}**. Está listo/a para el amor y "
            f"necesita un humano que entienda su régimen de cuidado y paciencia."
        )

    # *** Lógica de API Real (Solo se ejecuta con una clave válida) ***
    print(f"\nREAL: Generando Biografía para {nombre} a través de OpenAI...")
    
    # Prepara el 'prompt' para la IA
    prompt = f"""
    Eres un redactor de biografía para una app de adopción de mascotas. 
    Tu objetivo es convertir los datos crudos en una biografía emocional y atractiva, 
    máximo 60 palabras. 
    Asegúrate de incluir su Condición Especial y la REGLA OBLIGATORIA más importante.
    
    Datos del Animal (separados por ';'):
    {datos_animal}
    
    Tu biografía debe seguir este formato:
    Nombre (Edad) es una [Especie] [Raza] con... [Aquí la biografía emocionante, usando la Condición Especial y la regla de Apto_Con].
    """
    
    try:
        # Petición a la API (usando el modelo estándar para simulación)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Actúas como un redactor de biografía de adopción experto, creando textos emocionales y concisos."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        
        # Devuelve el texto generado
        return completion.choices[0].message.content.strip()

    except Exception as e:
        # En caso de error (ej. límite de uso excedido)
        return f"***ERROR DE GENERACIÓN IA: {e}***"

# -----------------------------------------------------------
# 3. Procesamiento y Simulación
# -----------------------------------------------------------
def procesar_dataset_simulacion(archivo_csv):
    """Carga los datos y simula la generación de biografías para los animales."""
    try:
        # Leer el CSV (usando el punto y coma como separador y manejando el cambio de columna)
        df = pd.read_csv(archivo_csv, sep=';', header=None, encoding='utf-8')
        
        # Nombres de las columnas, ajustado al cambio de 'Palabras_Clave_Caracter' por 'Caracter_Necesidad'
        df.columns = [
            'Nombre', 'Especie', 'Raza', 'Sexo', 'Edad_Años', 'Peso', 'Tamaño', 
            'Color_Pelaje', 'Apto_Con', 'Condicion_Especial', 'Desparasitado', 
            'Esterilizado', 'Con_Microchip', 'Vacunado', 'Adoptado', 
            'Caracter_Necesidad', 'Historia_Breve', 'Biografia_Final' # <--- CAMBIO AQUÍ
        ]
        
    except FileNotFoundError:
        print(f"\nError: El archivo {archivo_csv} no se encuentra.")
        return
    except Exception as e:
        print(f"\nError al leer el archivo CSV. Comprueba el formato de punto y coma: {e}")
        return

    # Tomar, por ejemplo, los primeros 3 animales para la simulación
    print("-" * 60)
    print(f"*** SIMULACIÓN IA 3: Generación de Biografías para los primeros {min(3, len(df))} animales ***")
    
    # Iterar sobre las filas
    for index, row in df.head(3).iterrows():
        # Construye la cadena de datos clave para el prompt
        datos_clave = f"{row['Nombre']};{row['Raza']};{row['Edad_Años']};{row['Condicion_Especial']};{row['Apto_Con']}"
        
        # Llama a la función de IA (simulada o real)
        bio_generada = generar_bio_ia(datos_clave)
        
        # Muestra el resultado
        print("-" * 60)
        print(f"Datos de Entrada (Campos Clave):\n{datos_clave}")
        print("\nBiografía Generada por IA (Resultado):")
        print(bio_generada)
    
    print("-" * 60)


if __name__ == "__main__":
    # Asegúrate de que el nombre del archivo CSV sea correcto
    nombre_archivo_csv = "dataset_adopcion.csv" 
    
    # Inicia la simulación
    procesar_dataset_simulacion(nombre_archivo_csv)