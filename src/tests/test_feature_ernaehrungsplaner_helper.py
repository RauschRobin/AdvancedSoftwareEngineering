def test_success_dinner_message_builder():
    # 1. Setup Test Environment
    builder = DinnerMessageBuilder()

    # 2. Simulate Building Process
    builder.add_meal_name("Spaghetti Carbonara")
    builder.add_meal_category("Italienische Küche")
    builder.add_meal_to_buy_ingredients(["Speck", "Eier", "Parmesan"])

    # 3. Retrieve the Built Product
    sentence = builder.sentence

    # 4. Define Expected Outcome
    expected_sentence = "Du kannst heute Spaghetti Carbonara kochen. " \
                        "Das essen gehört zur Kategorie Italienische Küche. " \
                        "Für dieses Gericht musst du noch Speck, Eier und Parmesan kaufen."

    # 5. Assertion
    # Assuming Sentence1 implements __str__ method
    assert str(sentence) == expected_sentence

    # 6. Reset Behavior Check (Optional)
    builder.add_meal_name("Pizza")
    new_sentence = builder.sentence
    # New sentence should be different
    assert str(new_sentence) != expected_sentence
