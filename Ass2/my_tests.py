from classes2 import NumberPlate
from hashing import ChainingHashTable  # Replace with actual module name


def test_basic_insert_and_retrieve():
    print("Test: Basic Insert and Retrieve")
    table = ChainingHashTable(5)
    
    plate1 = NumberPlate('ABC123')
    plate2 = NumberPlate('XYZ999')
    table[plate1] = 'Flag 1'
    table[plate2] = 'Flag 2'
    
    assert plate1 in table
    assert plate2 in table
    assert table[plate1] == 'Flag 1'
    assert table[plate2] == 'Flag 2'
    
    print(table)
    print("Passed ✅\n")


def test_chaining_behavior():
    print("Test: Chaining Behavior (Collisions)")
    table = ChainingHashTable(2)  # Force collisions

    plate1 = NumberPlate('AAA000')
    plate2 = NumberPlate('BBB111')
    plate3 = NumberPlate('CCC222')

    table[plate1] = 'First'
    table[plate2] = 'Second'
    table[plate3] = 'Third'

    print(table)
    for plate in [plate1, plate2, plate3]:
        assert plate in table
        print(f"{plate} -> {table[plate]}")
    
    print("Passed ✅\n")


def test_update_value():
    print("Test: Updating Existing Value")
    table = ChainingHashTable(5)
    plate = NumberPlate('ABC321')
    
    table[plate] = 'Initial'
    assert table[plate] == 'Initial'

    table[plate] = 'Updated'
    assert table[plate] == 'Updated'
    
    print(table)
    print("Passed ✅\n")


def test_condensed_str():
    print("Test: Condensed String Output")
    table = ChainingHashTable(3)
    
    plate1 = NumberPlate('ABC123')
    plate2 = NumberPlate('DEF456')
    table[plate1] = 'Data1'
    table[plate2] = 'Data2'

    print(table.condensed_str())
    print("Passed ✅\n")


if __name__ == '__main__':
    test_basic_insert_and_retrieve()
    test_chaining_behavior()
    test_update_value()
    test_condensed_str()
