"""Exemple documentaire de détection d'objets avec YOLOv8."""

from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def detect_objects(image):
    """Détecte les objets présents dans une image."""
    results = model(image)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            print(f"Objet détecté : classe={class_id}, confiance={confidence:.2f}")

    return results


if __name__ == "__main__":
    print("Module de détection YOLOv8 - prototype documentaire")
