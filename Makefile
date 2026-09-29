CONTENT_DIR 	:= ./content
CV_CONTENTS 	:= $(CONTENT_DIR)/experience.yaml $(CONTENT_DIR)/projects.yaml \
					$(CONTENT_DIR)/skills.yaml $(CONTENT_DIR)/education.yaml

TEMPLATE_DIR	:= ./src/templates
BASE_TEMPLATE	:= $(TEMPLATE_DIR)/base.html.jinja
CV_TEMPLATES	:= $(wildcard $(TEMPLATE_DIR)/cv/*.jinja)

REQUIRED    	:= $(CONTENT_DIR)/socials.yaml $(BASE_TEMPLATE)

BUILD_DIR   	:= ./build

all: $(BUILD_DIR)/index.html $(BUILD_DIR)/about-me.html $(BUILD_DIR)/cv.html

$(BUILD_DIR)/cv.html: $(CV_TEMPLATES) $(CV_CONTENTS) $(REQUIRED)
	uv run render_cv

$(BUILD_DIR)/%.html: $(TEMPLATE_DIR)/%.html.jinja $(REQUIRED)
	uv run render_template $(<F)
