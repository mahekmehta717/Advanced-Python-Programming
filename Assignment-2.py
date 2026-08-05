def bold_text(func):
    def wrapper(report):
        return "**" + func(report) + "**"
    return wrapper


class Report:
    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template):
        cls.templates[name] = template

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    def __call__(self, template_name):
        template = self.get_template(template_name)
        if template:
            return template(self)
        return "Template not found"

    def __str__(self):
        return f"{self.title}\n{self.content}"


def simple_template(report):
    return f"{report.title}\n{report.content}"


@bold_text
def fancy_template(report):
    return f"{report.title}\n{report.content}"


def main():
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    report = Report("Monthly Report", "Sales increased by 20%.")

    print(report("simple"))
    print(report("fancy"))


if __name__ == "__main__":
    main()
