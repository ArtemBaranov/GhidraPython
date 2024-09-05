from ghidra.program.model.listing import FunctionManager

def main():
    prefixes = ['Ke', 'Ps', 'Se', 'Io', 'Ki', 'Cc', 'Mm', 'Mi', 'Ob', 'Cm', 'Ex', 'Hal', 'Po', 'Etw', 'Nt', 'Pi', 'Pnp', 'Ppm', 'Vf']
    size_dict = {prefix: 0 for prefix in prefixes}
    size_dict['Others'] = 0

    fm = currentProgram.getFunctionManager()
    functions = fm.getFunctions(True)

    total_size = 0.0  # Use float to avoid integer division issues

    for func in functions:
        func_name = func.getName()
        func_size = float(func.getBody().getNumAddresses())  # Cast to float for accurate division

        total_size += func_size
        matched = False
        for prefix in prefixes:
            if func_name.startswith(prefix):
                size_dict[prefix] += func_size
                matched = True
                break
        if not matched:
            size_dict['Others'] += func_size

    print("Function Size by Class:")
    print("=======================")
    for prefix in prefixes:
        size_kb = size_dict[prefix] / 1024  # Convert bytes to KB
        percentage = (size_dict[prefix] / total_size) * 100  # Calculate percentage
        print("{}: {:.2f} KB ({:.2f}%)".format(prefix, size_kb, percentage))
    
    others_kb = size_dict['Others'] / 1024
    others_percentage = (size_dict['Others'] / total_size) * 100
    print("Others: {:.2f} KB ({:.2f}%)".format(others_kb, others_percentage))

    total_size_kb = total_size / 1024
    print("=======================")
    print("Total size of all functions: {:.2f} KB".format(total_size_kb))

if __name__ == "__main__":
    main()
