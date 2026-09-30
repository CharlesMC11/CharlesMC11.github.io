CONTENT_DIR 	:= ./content
CV_CONTENT_DIR	:= $(CONTENT_DIR)/experience.yaml \
					$(CONTENT_DIR)/projects.yaml $(CONTENT_DIR)/skills.yaml \
					$(CONTENT_DIR)/education.yaml

TEMPLATES_DIR	:= ./src/templates
BASE_TEMPLATE	:= $(TEMPLATES_DIR)/base.html.jinja
CV_TEMPLATES	:= $(wildcard $(TEMPLATES_DIR)/cv/*.jinja)

GLOBAL_DEPS 	:= $(CONTENT_DIR)/socials.yaml $(BASE_TEMPLATE) ./src/build.py

BUILD_DIR   	:= ./build

all: $(BUILD_DIR)/index.html $(BUILD_DIR)/about-me.html $(BUILD_DIR)/cv.html \
		$(BUILD_DIR)/style.css

$(BUILD_DIR)/cv.html: $(CV_TEMPLATES) $(CV_CONTENT_DIR) $(GLOBAL_DEPS)
	uv run build_cv

$(BUILD_DIR)/%.html: $(TEMPLATES_DIR)/%.html.jinja $(GLOBAL_DEPS)
	uv run build_page $(<F)

$(BUILD_DIR)/style.css: ./src/static/style.css.jinja ./src/build.py
	uv run build_css

check:
	@uvx ruff check .
	@uvx ruff format --check .
