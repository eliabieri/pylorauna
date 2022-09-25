from pylorauna.lorauna import LoraunaClient

def main():
    client = LoraunaClient()
    data = client.get_data()
    print(data.capacity_message)

if __name__ == "__main__":
    main()