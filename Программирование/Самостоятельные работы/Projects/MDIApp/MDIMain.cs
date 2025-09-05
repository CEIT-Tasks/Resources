namespace MDIApp
{
  public partial class MDIMain : Form
  {
    public int lastNum = 1;
    public MDIMain()
    {
      InitializeComponent();
    }

    private void newToolStripMenuItem_Click(object sender, EventArgs e)
    {
      Daughter daughter = new(lastNum);
      lastNum++;
      daughter.MdiParent = this;
      daughter.Show();
    }

    private void cascadeToolStripMenuItem_Click(object sender, EventArgs e)
    {
      LayoutMdi(MdiLayout.Cascade);
    }

    private void tileHorizontallyToolStripMenuItem_Click(object sender, EventArgs e)
    {
      LayoutMdi(MdiLayout.TileHorizontal);
    }

    private void tileVerticallyToolStripMenuItem_Click(object sender, EventArgs e)
    {
      LayoutMdi(MdiLayout.TileVertical);
    }

    private void closeToolStripMenuItem_Click(object sender, EventArgs e)
    {
      if (MdiChildren.Length > 0)
        ActiveMdiChild?.Close();
    }

    private void exitToolStripMenuItem_Click(object sender, EventArgs e)
    {
      Close();
    }

    private void closeAllToolStripMenuItem_Click(object sender, EventArgs e)
    {
      foreach (var form in MdiChildren) form.Close();
    }

    private void MDIMain_Load(object sender, EventArgs e)
    {

    }

    private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
    {
      MessageBox.Show("This is an MDI app", "About", MessageBoxButtons.OK, 
        MessageBoxIcon.Information);
    }
  }
}
