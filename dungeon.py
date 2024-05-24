def read_input():
    inputs = []
    
    while True:
        # Read dimensions
        line = input().strip()
        if not line:
            continue  # Skip any empty lines
        L, R, C = map(int, line.split())
        
        # Break if dimensions are 0 0 0
        if L == 0 and R == 0 and C == 0:
            break
        
        # Read the grid for the given dimensions
        grid = []
        for _ in range(L):
            layer = []
            for _ in range(R):
                layer.append(input().strip())
            waste = input()
            grid.append(layer)
        
        inputs.append((L, R, C, grid))
    
    return inputs

def main():
    inputs = read_input()
    for L, R, C, grid in inputs:
        print(f'Dimensions: L={L}, R={R}, C={C}')
        for layer in grid:
            for row in layer:
                print(row)
            print()  # Separate layers by a blank line

if __name__ == "__main__":
    main()
