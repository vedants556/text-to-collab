import wx
from datetime import datetime
from text_parser import parse_text_to_cells
from notebook_creator import create_notebook, save_notebook

class TextToNotebookApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Text to Jupyter Notebook Converter", size=(600, 400), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        # Set light mode colors
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.SetForegroundColour(wx.Colour(0, 0, 0))

        # Create a panel for layout
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        # Rounded corners - using a wx.GraphicsContext
        self.Bind(wx.EVT_PAINT, self.on_paint)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Text area for user input
        self.text_area = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_PROCESS_ENTER)
        self.text_area.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_area.SetForegroundColour(wx.Colour(0, 0, 0))
        self.text_area.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        vbox.Add(self.text_area, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Entry for notebook name
        self.filename_label = wx.StaticText(panel, label="Enter notebook name (without extension):")
        self.filename_label.SetForegroundColour(wx.Colour(0, 0, 0))
        vbox.Add(self.filename_label, flag=wx.LEFT | wx.TOP, border=10)

        self.filename_entry = wx.TextCtrl(panel)
        self.filename_entry.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.filename_entry.SetForegroundColour(wx.Colour(0, 0, 0))
        vbox.Add(self.filename_entry, flag=wx.LEFT | wx.EXPAND | wx.BOTTOM, border=10)

        # Button to save notebook
        self.save_button = wx.Button(panel, label="Save Notebook")
        self.save_button.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.save_button.SetForegroundColour(wx.Colour(0, 0, 0))
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save_notebook)
        vbox.Add(self.save_button, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)

        panel.SetSizer(vbox)
        self.Show()

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)
        gc.SetBrush(wx.Brush(wx.Colour(255, 255, 255)))
        gc.DrawRoundedRectangle(0, 0, self.GetSize().width, self.GetSize().height, 20)

    def on_save_notebook(self, event):
        input_text = self.text_area.GetValue().strip()
        base_filename = self.filename_entry.GetValue().strip() or "notebook"

        if not input_text:
            wx.MessageBox("Please enter some text.", "Input Error", wx.OK | wx.ICON_WARNING)
            return

        # Parse the input text and create notebook
        cells = parse_text_to_cells(input_text)
        notebook = create_notebook(cells)

        # Generate a unique filename
        unique_filename = self.get_unique_filename(base_filename)

        # Save the notebook
        save_notebook(notebook, unique_filename)

    def get_unique_filename(self, base_filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{base_filename}_{timestamp}.ipynb"

if __name__ == "__main__":
    app = wx.App(False)
    TextToNotebookApp()
    app.MainLoop()
