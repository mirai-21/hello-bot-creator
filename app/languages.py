def languages(
    selected_exchange: str = "",
    selected_keywords: str = "",
    selected_frequency: str = "",
    new_projects: bool = False,
):
    return {
        "ua": {
            "ua_start": {
                "text": "👋 Вітаю! Я бот, який допоможе відслідковувати нові проєкти з різних фріланс-бірж.\nЩо хочете зробити?!",
                "buttons": [
                    {"text": "🔍 Обрати біржі", "callback_data": "ua_select_exchange"},
                    {"text": "⚙ Налаштування", "callback_data": "ua_settings"},
                    {"text": "ℹ Допомога", "callback_data": "ua_help"},
                ],
            },
            "ua_settings": {
                "text": f"[⚙ Налаштування\n🔍 Обрані біржі: {selected_exchange}\n📝 Ключові слова: {selected_keywords}\n⏱ Частота перевірок: {selected_frequency}\n\nЩо хочете змінити?",
                "buttons": [
                    {
                        "text": "🔍 Біржі",
                        "callback_data": "ua_settings_exchanges",
                    },
                    {
                        "text": "📝 Ключові слова",
                        "callback_data": "ua_settings_keywords",
                    },
                    {
                        "text": "🔔 Сповіщення",
                        "callback_data": "ua_settings_notifications",
                    },
                    {
                        "text": "⬅ Назад",
                        "callback_data": "ua_back",
                    },
                ],
            },
            "ua_notifications": {
                "text": f"[🔔 Сповіщення]\n\nСповіщення про нові проєкти",
                "buttons": [
                    {
                        "text": "🔘 Увімкнені" if new_projects else "⚪ Увімкнені",
                        "callback_data": "ua_notifications_enabled",
                    },
                    {
                        "text": "⚪ Вимкнені" if not new_projects else "🔘 Вимкнені",
                        "callback_data": "ua_notifications_disabled",
                    },
                    {"text": "⬅ Назад", "callback_data": "ua_settings"},
                ],
            },
            "ua_exchanges": {
                "text": f"Оберіть фріланс-біржі: {selected_exchange}",
                "buttons": [
                    {"text": "💾 Зберегти", "callback_data": "ua_save_exchanges"},
                    {"text": "⬅ Назад", "callback_data": "ua_settings"},
                ],
            },
        }
    }
