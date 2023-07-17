import nbformat as nbf

def guardar_resultados_en_ipynb(accuracy, conf_matrix, classification_rep, ruta_destino, nombre_archivo):
    # Crear un nuevo cuaderno en blanco
    nb = nbf.v4.new_notebook()

    # Agregar una celda de texto con los resultados en formato Markdown
    markdown = f"# Resultados\n\n"
    markdown += f"**Accuracy**: {accuracy}\n\n"
    markdown += f"**Confusion Matrix**:\n\n"
    markdown += "```\n"
    markdown += f"{conf_matrix}\n"
    markdown += "```\n\n"
    markdown += f"**Classification Report**:\n\n"
    markdown += "```\n"
    markdown += f"{classification_rep}\n"
    markdown += "```\n"

    text_cell = nbf.v4.new_markdown_cell(markdown)
    nb.cells.append(text_cell)

    # Guardar el cuaderno en la ubicación especificada
    nbf.write(nb, open(ruta_destino + nombre_archivo, 'w'), version=nbf.NO_CONVERT)

