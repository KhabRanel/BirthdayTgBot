from services.storage_json import load_birthdays


birthdays: dict[int, dict[str, str]] = load_birthdays()