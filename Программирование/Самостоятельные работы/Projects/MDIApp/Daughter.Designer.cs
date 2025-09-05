namespace MDIApp
{
  partial class Daughter
  {
    /// <summary>
    /// Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    /// Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
      if (disposing && (components != null))
      {
        components.Dispose();
      }
      base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    /// Required method for Designer support - do not modify
    /// the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
      textBox1 = new TextBox();
      menuStrip2 = new MenuStrip();
      fileToolStripMenuItem = new ToolStripMenuItem();
      openToolStripMenuItem = new ToolStripMenuItem();
      openFileDialog = new OpenFileDialog();
      menuStrip2.SuspendLayout();
      SuspendLayout();
      // 
      // textBox1
      // 
      textBox1.Dock = DockStyle.Fill;
      textBox1.Location = new Point(0, 24);
      textBox1.Multiline = true;
      textBox1.Name = "textBox1";
      textBox1.Size = new Size(800, 426);
      textBox1.TabIndex = 0;
      // 
      // menuStrip2
      // 
      menuStrip2.Items.AddRange(new ToolStripItem[] { fileToolStripMenuItem });
      menuStrip2.Location = new Point(0, 0);
      menuStrip2.Name = "menuStrip2";
      menuStrip2.Size = new Size(800, 24);
      menuStrip2.TabIndex = 1;
      menuStrip2.Text = "menuStrip1";
      // 
      // fileToolStripMenuItem
      // 
      fileToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { openToolStripMenuItem });
      fileToolStripMenuItem.MergeAction = MergeAction.Insert;
      fileToolStripMenuItem.Name = "fileToolStripMenuItem";
      fileToolStripMenuItem.Size = new Size(37, 20);
      fileToolStripMenuItem.Text = "File";
      // 
      // openToolStripMenuItem
      // 
      openToolStripMenuItem.Name = "openToolStripMenuItem";
      openToolStripMenuItem.Size = new Size(180, 22);
      openToolStripMenuItem.Text = "Open";
      openToolStripMenuItem.Click += openToolStripMenuItem_Click_1;
      // 
      // openFileDialog
      // 
      openFileDialog.FileName = "openFileDialog";
      openFileDialog.FileOk += openFileDialog_FileOk;
      // 
      // Daughter
      // 
      AutoScaleDimensions = new SizeF(7F, 15F);
      AutoScaleMode = AutoScaleMode.Font;
      ClientSize = new Size(800, 450);
      Controls.Add(textBox1);
      Controls.Add(menuStrip2);
      MainMenuStrip = menuStrip2;
      Name = "Daughter";
      Text = "Daugther";
      menuStrip2.ResumeLayout(false);
      menuStrip2.PerformLayout();
      ResumeLayout(false);
      PerformLayout();
    }

    #endregion

    private TextBox textBox1;
    private MenuStrip menuStrip2;
    private ToolStripMenuItem fileToolStripMenuItem;
    private ToolStripMenuItem openToolStripMenuItem;
    private OpenFileDialog openFileDialog;
  }
}