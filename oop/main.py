from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)          # __str__ output
    print(repr(my_book))    # __repr__ output
    del my_book             # triggers __del__

if __name__ == "__main__":
    main()


# main.py
from polymorphism_demo import Rectangle, Circle

def main():
    shapes = []

    try:
        shapes.append(Rectangle(10, 5))
        shapes.append(Circle(7))
        shapes.append(Rectangle(-3, 4))  # This will trigger ValueError
        shapes.append(Circle("abc"))     # This will trigger TypeError
    except (ValueError, TypeError) as e:
        print(f"Error creating shape: {e}")

    print("\nCalculating areas of valid shapes:")
    for shape in shapes:
        try:
            print(f"Area: {shape.area():.2f}")
        except Exception as e:
            print(f"Error calculating area: {e}")

if __name__ == "__main__":
    main()




from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
