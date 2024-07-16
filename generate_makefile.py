import os

TEMPLATE_CONTENT = """
################################################################################
# Automatically-generated file. Do not edit!
################################################################################

RM := rm -rf

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS := {{SRC_FILES}}
OBJS := {{OBJ_FILES}}
CPP_DEPS := {{DEP_FILES}}

# Specify the compiler and compiler flags
CC := C:/ETK/L17.02/usr/bin/c89.exe
CFLAGS := -g -Wcplusplus -Woptimize=1 -Wsystype=oss -Wcall_shared

# All Target
all: {{TARGET_NAME}}.txe

# Tool invocations
{{TARGET_NAME}}.txe: $(OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: C++ Linker (TNS/E)'
	$(CC) $(CFLAGS) -o "$@" $(OBJS)
	@echo 'Finished building target: $@'
	@echo ' '

# Each subdirectory must supply rules for building sources it contributes
{{OBJ_FILES}}: {{SRC_FILES}}
	@echo 'Building file: $<'
	@echo 'Invoking: C++ Compiler (TNS/E)'
	$(CC) $(CFLAGS) -c -o "$@" "$<" && \\
	$(CC) $(CFLAGS) -c -WM "$<" | grep -v -e '$(NSDEE_SYS_INCLUDE_PATH_ESC)' -e 'test.cpp' | sed -e 's/[ ].*test\\\\Debug\\\\\\.\\./ ..\\//g' > {{DEP_FILES}}
	@echo 'Finished building: $<'
	@echo ' '

# Other Targets
clean:
	-$(RM) $(OBJS) $(CPP_DEPS) $(CPP_SRCS) {{TARGET_NAME}}.txe
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY:
"""

def generate_makefile():
    # Get the target name from the current directory
    target_name = os.path.basename(os.getcwd())

    # Find all source files in the src directory
    src_files = " ".join([os.path.join("src", f) for f in os.listdir("src") if f.endswith(".cpp")])
    obj_files = " ".join([os.path.join("src", f.replace(".cpp", ".o")) for f in os.listdir("src") if f.endswith(".cpp")])
    dep_files = " ".join([os.path.join("src", f.replace(".cpp", ".d")) for f in os.listdir("src") if f.endswith(".cpp")])

    # Replace placeholders with actual values
    makefile_content = TEMPLATE_CONTENT.replace("{{SRC_FILES}}", src_files)
    makefile_content = makefile_content.replace("{{OBJ_FILES}}", obj_files)
    makefile_content = makefile_content.replace("{{DEP_FILES}}", dep_files)
    makefile_content = makefile_content.replace("{{TARGET_NAME}}", target_name)

    # Write the Makefile
    with open("Makefile", "w") as file:
        file.write(makefile_content)

    print("Makefile generated successfully.")

if __name__ == "__main__":
    if not os.path.exists("src"):
        print("Error: 'src' directory does not exist.")
        exit(1)
    generate_makefile()
