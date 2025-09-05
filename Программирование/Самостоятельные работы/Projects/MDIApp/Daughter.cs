using System.ComponentModel;

namespace MDIApp
{
  public partial class Daughter : Form
  {
    public Daughter(int num)
    {
      InitializeComponent();
      Text = "MDI" + num;
    }

    private void openToolStripMenuItem_Click_1(object sender, EventArgs e)
    {
      openFileDialog.ShowDialog();
    }

    private void openFileDialog_FileOk(object sender, CancelEventArgs e)
    {
      try
      {
        using (StreamReader sr = new(openFileDialog.FileName))
        {
          textBox1.Text = sr.ReadToEnd();
        }
      }
      catch (Exception ex)
      {
        MessageBox.Show("Error reading file: " + ex.Message);
      }
    }
  }
}
