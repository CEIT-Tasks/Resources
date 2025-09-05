namespace MDIApp
{
  partial class MDIMain
  {
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
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
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
      menuStrip1 = new MenuStrip();
      fileToolStripMenuItem = new ToolStripMenuItem();
      newToolStripMenuItem = new ToolStripMenuItem();
      closeToolStripMenuItem = new ToolStripMenuItem();
      closeAllToolStripMenuItem = new ToolStripMenuItem();
      exitToolStripMenuItem = new ToolStripMenuItem();
      windowToolStripMenuItem = new ToolStripMenuItem();
      cascadeToolStripMenuItem = new ToolStripMenuItem();
      tileHorizontallyToolStripMenuItem = new ToolStripMenuItem();
      tileVerticallyToolStripMenuItem = new ToolStripMenuItem();
      helpToolStripMenuItem = new ToolStripMenuItem();
      aboutToolStripMenuItem = new ToolStripMenuItem();
      menuStrip1.SuspendLayout();
      SuspendLayout();
      // 
      // menuStrip1
      // 
      menuStrip1.Items.AddRange(new ToolStripItem[] { fileToolStripMenuItem, windowToolStripMenuItem, helpToolStripMenuItem });
      menuStrip1.Location = new Point(0, 0);
      menuStrip1.Name = "menuStrip1";
      menuStrip1.Size = new Size(800, 24);
      menuStrip1.TabIndex = 1;
      menuStrip1.Text = "menuStrip1";
      // 
      // fileToolStripMenuItem
      // 
      fileToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { newToolStripMenuItem, closeToolStripMenuItem, closeAllToolStripMenuItem, exitToolStripMenuItem });
      fileToolStripMenuItem.Name = "fileToolStripMenuItem";
      fileToolStripMenuItem.Size = new Size(37, 20);
      fileToolStripMenuItem.Text = "File";
      // 
      // newToolStripMenuItem
      // 
      newToolStripMenuItem.Name = "newToolStripMenuItem";
      newToolStripMenuItem.Size = new Size(180, 22);
      newToolStripMenuItem.Text = "New";
      newToolStripMenuItem.Click += newToolStripMenuItem_Click;
      // 
      // closeToolStripMenuItem
      // 
      closeToolStripMenuItem.Name = "closeToolStripMenuItem";
      closeToolStripMenuItem.Size = new Size(180, 22);
      closeToolStripMenuItem.Text = "Close";
      closeToolStripMenuItem.Click += closeToolStripMenuItem_Click;
      // 
      // closeAllToolStripMenuItem
      // 
      closeAllToolStripMenuItem.Name = "closeAllToolStripMenuItem";
      closeAllToolStripMenuItem.Size = new Size(180, 22);
      closeAllToolStripMenuItem.Text = "Close All";
      closeAllToolStripMenuItem.Click += closeAllToolStripMenuItem_Click;
      // 
      // exitToolStripMenuItem
      // 
      exitToolStripMenuItem.Name = "exitToolStripMenuItem";
      exitToolStripMenuItem.Size = new Size(180, 22);
      exitToolStripMenuItem.Text = "Exit";
      exitToolStripMenuItem.Click += exitToolStripMenuItem_Click;
      // 
      // windowToolStripMenuItem
      // 
      windowToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { cascadeToolStripMenuItem, tileHorizontallyToolStripMenuItem, tileVerticallyToolStripMenuItem });
      windowToolStripMenuItem.Name = "windowToolStripMenuItem";
      windowToolStripMenuItem.Size = new Size(63, 20);
      windowToolStripMenuItem.Text = "Window";
      // 
      // cascadeToolStripMenuItem
      // 
      cascadeToolStripMenuItem.Name = "cascadeToolStripMenuItem";
      cascadeToolStripMenuItem.Size = new Size(158, 22);
      cascadeToolStripMenuItem.Text = "Cascade";
      cascadeToolStripMenuItem.Click += cascadeToolStripMenuItem_Click;
      // 
      // tileHorizontallyToolStripMenuItem
      // 
      tileHorizontallyToolStripMenuItem.Name = "tileHorizontallyToolStripMenuItem";
      tileHorizontallyToolStripMenuItem.Size = new Size(158, 22);
      tileHorizontallyToolStripMenuItem.Text = "Tile horizontally";
      tileHorizontallyToolStripMenuItem.Click += tileHorizontallyToolStripMenuItem_Click;
      // 
      // tileVerticallyToolStripMenuItem
      // 
      tileVerticallyToolStripMenuItem.Name = "tileVerticallyToolStripMenuItem";
      tileVerticallyToolStripMenuItem.Size = new Size(158, 22);
      tileVerticallyToolStripMenuItem.Text = "Tile vertically";
      tileVerticallyToolStripMenuItem.Click += tileVerticallyToolStripMenuItem_Click;
      // 
      // helpToolStripMenuItem
      // 
      helpToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { aboutToolStripMenuItem });
      helpToolStripMenuItem.Name = "helpToolStripMenuItem";
      helpToolStripMenuItem.Size = new Size(44, 20);
      helpToolStripMenuItem.Text = "Help";
      // 
      // aboutToolStripMenuItem
      // 
      aboutToolStripMenuItem.Name = "aboutToolStripMenuItem";
      aboutToolStripMenuItem.Size = new Size(180, 22);
      aboutToolStripMenuItem.Text = "About";
      aboutToolStripMenuItem.Click += aboutToolStripMenuItem_Click;
      // 
      // MDIMain
      // 
      AutoScaleDimensions = new SizeF(7F, 15F);
      AutoScaleMode = AutoScaleMode.Font;
      ClientSize = new Size(800, 450);
      Controls.Add(menuStrip1);
      IsMdiContainer = true;
      MainMenuStrip = menuStrip1;
      Name = "MDIMain";
      Text = "MDIApp";
      Load += MDIMain_Load;
      menuStrip1.ResumeLayout(false);
      menuStrip1.PerformLayout();
      ResumeLayout(false);
      PerformLayout();
    }

    #endregion

    private MenuStrip menuStrip1;
    private ToolStripMenuItem fileToolStripMenuItem;
    private ToolStripMenuItem newToolStripMenuItem;
    private ToolStripMenuItem closeToolStripMenuItem;
    private ToolStripMenuItem closeAllToolStripMenuItem;
    private ToolStripMenuItem exitToolStripMenuItem;
    private ToolStripMenuItem windowToolStripMenuItem;
    private ToolStripMenuItem cascadeToolStripMenuItem;
    private ToolStripMenuItem tileHorizontallyToolStripMenuItem;
    private ToolStripMenuItem tileVerticallyToolStripMenuItem;
    private ToolStripMenuItem helpToolStripMenuItem;
    private ToolStripMenuItem aboutToolStripMenuItem;
  }
}
