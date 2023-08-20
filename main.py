from api.external_api import fetch_data_from_external_api, get_first_entry_attribute


def main():
    while True:

        user_input = input("Enter a word (type 'exit' to quit): ")

        data = fetch_data_from_external_api(user_input)
        attribute_value = get_first_entry_attribute(data)
        print(attribute_value)

        if user_input.lower() == 'exit':
            print("Exiting the program...")
            break


if __name__ == "__main__":
    main()
