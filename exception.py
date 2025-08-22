try:
    infile = input("Enter file to read: ")
    with open(infile, "r") as f:
        data = f.read()
    outfile = input("Enter new file name: ")
    with open(outfile, "w") as f:
        f.write(data.upper())   # modify here
    print("Done! File saved as", outfile)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)