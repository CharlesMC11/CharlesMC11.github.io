TEMPLATE_DIR	:= ./src/templates
CV_TEMPLATES	:= $(wildcard $(TEMPLATE_DIR)/cv/*.jinja)

BUILD_DIR   	:= ./build

all: $(BUILD_DIR)/index.html $(BUILD_DIR)/about-me.html $(BUILD_DIR)/cv.html

$(BUILD_DIR)/cv.html: $(CV_TEMPLATES) $(TEMPLATE_DIR)/base.html.jinja
	uv run render_cv

$(BUILD_DIR)/%.html: $(TEMPLATE_DIR)/%.html.jinja $(TEMPLATE_DIR)/base.html.jinja
	uv run render_template $(<F)
