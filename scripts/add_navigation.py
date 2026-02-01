
import os

# Base path
BASE_PATH = "/Users/lic.ing.jesusolvera/Documents/PROYECTOS PERSONALES/SKILLS-ISC-TECNM/simulacion-tecnm/content"

# Define order of files
ORDER = [
    # Unidad 1
    ("unidad1", "README.md", "Inicio Unidad 1"),
    ("unidad1", "1.1.md", "1.1 Conceptos Básicos"),
    ("unidad1", "1.2.md", "1.2 Áreas de Aplicación"),
    ("unidad1", "1.3.md", "1.3 Sistemas y Modelos"),
    ("unidad1", "1.4.md", "1.4 Fases del Estudio"),
    ("unidad1", "1.5.md", "1.5 Metodología"),
    ("unidad1", "1.6.md", "1.6 Componentes DES"),
    ("unidad1", "1.7.md", "1.7 Decisión de Uso"),
    
    # Unidad 2
    ("unidad2", "README.md", "Inicio Unidad 2"),
    ("unidad2", "2.1.md", "2.1 Generación de Números"),
    ("unidad2", "2.2.md", "2.2 Pruebas de Validación"),
    ("unidad2", "2.2.1.md", "2.2.1 Uniformidad"),
    ("unidad2", "2.2.2.md", "2.2.2 Aleatoriedad"),
    ("unidad2", "2.2.3.md", "2.2.3 Independencia"),
    ("unidad2", "2.3.md", "2.3 Monte Carlo"),
    ("unidad2", "2.3.1.md", "2.3.1 Características"),
    ("unidad2", "2.3.2.md", "2.3.2 Aplicaciones"),
    ("unidad2", "2.3.3.md", "2.3.3 Solución Problemas"),

    # Unidad 3
    ("unidad3", "README.md", "Inicio Unidad 3"),
    ("unidad3", "3.1.md", "3.1 Conceptos VA"),
    ("unidad3", "3.2.md", "3.2 VA Discretas"),
    ("unidad3", "3.3.md", "3.3 VA Continuas"),
    ("unidad3", "3.4.md", "3.4 Métodos Generación"),
    ("unidad3", "3.4.1.md", "3.4.1 Transformada Inversa"),
    ("unidad3", "3.4.2.md", "3.4.2 Convolución"),
    ("unidad3", "3.4.3.md", "3.4.3 Composición"),
    ("unidad3", "3.5.md", "3.5 Procedimientos Especiales"),
    ("unidad3", "3.6.md", "3.6 Pruebas Estadísticas"),

    # Unidad 4
    ("unidad4", "README.md", "Inicio Unidad 4"),
    ("unidad4", "4.1.md", "4.1 Lenguajes"),
    ("unidad4", "4.2.md", "4.2 Aprendizaje"),
    ("unidad4", "4.3.md", "4.3 Casos Prácticos"),
    ("unidad4", "4.3.1.md", "4.3.1 Líneas de Espera"),
    ("unidad4", "4.3.2.md", "4.3.2 Inventarios"),
    ("unidad4", "4.4.md", "4.4 Validación"),
    ("unidad4", "4.4.1.md", "4.4.1 Paramétricas"),
    ("unidad4", "4.4.2.md", "4.4.2 No Paramétricas"),

    # Unidad 5
    ("unidad5", "README.md", "Inicio Unidad 5"),
    ("unidad5", "5.1.md", "5.1 Proyecto Integrador"),
]

def get_rel_path(from_unit, to_unit, to_file):
    if from_unit == to_unit:
        return to_file
    return f"../{to_unit}/{to_file}"

def add_nav_footer():
    for i in range(len(ORDER)):
        current_unit, current_file, current_title = ORDER[i]
        
        # Determine previous
        prev_link = None
        if i > 0:
            prev_unit, prev_file, prev_title = ORDER[i-1]
            path = get_rel_path(current_unit, prev_unit, prev_file)
            prev_link = f"⬅️ [{prev_title}]({path})"
        else:
            prev_link = "⬅️ [Inicio del Curso](../../README.md)"

        # Determine next
        next_link = None
        if i < len(ORDER) - 1:
            next_unit, next_file, next_title = ORDER[i+1]
            path = get_rel_path(current_unit, next_unit, next_file)
            next_link = f"[{next_title}]({path}) ➡️"
        else:
            next_link = "[Fin del Curso](../../README.md) 🏁"

        # Build footer
        footer = "\n\n---\n\n<div align=\"center\">\n\n"
        footer += f"{prev_link} &nbsp;&nbsp;|&nbsp;&nbsp; {next_link}"
        footer += "\n\n</div>\n"

        # File path
        file_path = os.path.join(BASE_PATH, current_unit, current_file)
        
        try:
            with open(file_path, "r") as f:
                content = f.read()
            
            # Remove existing footer if present (simple heuristic)
            if "<div align=\"center\">" in content and "⬅️" in content:
                # Assuming footer is at the end, find the split point
                split_content = content.rsplit("\n\n---\n\n<div align=\"center\">", 1)
                if len(split_content) > 1:
                   content = split_content[0]
            
            # Also check for the manual navigation I added to unit READMEs and strip it to avoid duplicates
            if "**Navegación:**" in content:
                 content = content.rsplit("**Navegación:**", 1)[0].strip()

            new_content = content + footer
            
            with open(file_path, "w") as f:
                f.write(new_content)
            
            print(f"Updated {current_file}")
            
        except Exception as e:
            print(f"Error updating {file_path}: {e}")

if __name__ == "__main__":
    add_nav_footer()
