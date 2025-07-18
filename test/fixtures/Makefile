# Variables
MESON_BUILD_DIR = builddir
NINJA = ninja

# Phony targets
.PHONY: setup_meson build_meson install_meson clean

# Default target
all: build_meson

$(MESON_BUILD_DIR):
	@mkdir -p $(MESON_BUILD_DIR)

# Setup Meson build directory
# Target to ensure meson.build is processed and builds are set up
setup_meson: $(MESON_BUILD_DIR)/build.ninja

# Rule to set up Meson build directory
$(MESON_BUILD_DIR)/build.ninja \
$(MESON_BUILD_DIR)/compile_commands.json: meson.build | $(MESON_BUILD_DIR)
	@meson setup $(MESON_BUILD_DIR)

# Build using Meson/Ninja
build_meson: $(MESON_BUILD_DIR)/build.ninja
	@$(NINJA) -C $(MESON_BUILD_DIR)

# Install binaries
install_meson: build_meson
	@$(NINJA) -C $(MESON_BUILD_DIR) install

# Clean build directory
clean::
	@rm -rf $(MESON_BUILD_DIR)

# Phony targets for Ninja
.PHONY: build_ninja install_ninja

# Build using Ninja directly from build.ninja
build_ninja: build.ninja | $(MESON_BUILD_DIR)
	@$(NINJA) -C $(MESON_BUILD_DIR) -f ../build.ninja

# Install binaries (assuming a similar install rule in build.ninja)
#install_ninja: $(MESON_BUILD_DIR) build.ninja
#	@$(NINJA) install
