TEMPLATE_DIR	:= ./src/templates
BASE_TEMPLATE	:= $(TEMPLATE_DIR)/base.html.jinja
CV_TEMPLATES	:= $(wildcard $(TEMPLATE_DIR)/cv/*.jinja)

BUILD_DIR   	:= ./build

all: $(BUILD_DIR)/index.html $(BUILD_DIR)/about-me.html $(BUILD_DIR)/cv.html

$(BUILD_DIR)/cv.html: $(CV_TEMPLATES) $(BASE_TEMPLATE)
	uv run render_cv

$(BUILD_DIR)/%.html: $(TEMPLATE_DIR)/%.html.jinja $(BASE_TEMPLATE)
	uv run render_template $(<F)
