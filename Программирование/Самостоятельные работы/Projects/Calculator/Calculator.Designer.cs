namespace Calculator
{
  partial class Calculator
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
      System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Calculator));
      textBox1 = new TextBox();
      textBox2 = new TextBox();
      label1 = new Label();
      label2 = new Label();
      button1 = new Button();
      button2 = new Button();
      button3 = new Button();
      button4 = new Button();
      button5 = new Button();
      SuspendLayout();
      // 
      // textBox1
      // 
      textBox1.Anchor = AnchorStyles.Top;
      textBox1.Location = new Point(12, 13);
      textBox1.Name = "textBox1";
      textBox1.Size = new Size(100, 23);
      textBox1.TabIndex = 0;
      // 
      // textBox2
      // 
      textBox2.Anchor = AnchorStyles.Top;
      textBox2.Location = new Point(139, 12);
      textBox2.Name = "textBox2";
      textBox2.Size = new Size(100, 23);
      textBox2.TabIndex = 1;
      // 
      // label1
      // 
      label1.Anchor = AnchorStyles.Top;
      label1.AutoSize = true;
      label1.Location = new Point(118, 15);
      label1.Name = "label1";
      label1.Size = new Size(0, 15);
      label1.TabIndex = 3;
      // 
      // label2
      // 
      label2.Anchor = AnchorStyles.Top;
      label2.AutoSize = true;
      label2.Location = new Point(245, 15);
      label2.Name = "label2";
      label2.Size = new Size(15, 15);
      label2.TabIndex = 4;
      label2.Text = "=";
      // 
      // button1
      // 
      button1.Anchor = AnchorStyles.Bottom;
      button1.Location = new Point(12, 76);
      button1.Name = "button1";
      button1.Size = new Size(40, 23);
      button1.TabIndex = 5;
      button1.Text = "+";
      button1.UseVisualStyleBackColor = true;
      button1.Click += button1_Click;
      // 
      // button2
      // 
      button2.Anchor = AnchorStyles.Bottom;
      button2.Location = new Point(58, 76);
      button2.Name = "button2";
      button2.Size = new Size(40, 23);
      button2.TabIndex = 6;
      button2.Text = "-";
      button2.UseVisualStyleBackColor = true;
      button2.Click += button2_Click;
      // 
      // button3
      // 
      button3.Anchor = AnchorStyles.Bottom;
      button3.Location = new Point(104, 76);
      button3.Name = "button3";
      button3.Size = new Size(40, 23);
      button3.TabIndex = 7;
      button3.Text = "*";
      button3.UseVisualStyleBackColor = true;
      button3.Click += button3_Click;
      // 
      // button4
      // 
      button4.Anchor = AnchorStyles.Bottom;
      button4.Location = new Point(150, 76);
      button4.Name = "button4";
      button4.Size = new Size(40, 23);
      button4.TabIndex = 8;
      button4.Text = "/";
      button4.UseVisualStyleBackColor = true;
      button4.Click += button4_Click;
      // 
      // button5
      // 
      button5.Anchor = AnchorStyles.Bottom;
      button5.Location = new Point(196, 76);
      button5.Name = "button5";
      button5.Size = new Size(64, 23);
      button5.TabIndex = 9;
      button5.Text = "=";
      button5.UseVisualStyleBackColor = true;
      button5.Click += button5_Click;
      // 
      // Calculator
      // 
      AutoScaleDimensions = new SizeF(7F, 15F);
      AutoScaleMode = AutoScaleMode.Font;
      ClientSize = new Size(484, 111);
      Controls.Add(button5);
      Controls.Add(button4);
      Controls.Add(button3);
      Controls.Add(button2);
      Controls.Add(button1);
      Controls.Add(label2);
      Controls.Add(label1);
      Controls.Add(textBox2);
      Controls.Add(textBox1);
      Icon = (Icon)resources.GetObject("$this.Icon");
      KeyPreview = true;
      MaximizeBox = false;
      MaximumSize = new Size(500, 150);
      MinimumSize = new Size(500, 150);
      Name = "Calculator";
      Text = "Калькулятор";
      ResumeLayout(false);
      PerformLayout();
    }

    #endregion

    private TextBox textBox1;
    private TextBox textBox2;
    private Label label1;
    private Label label2;
    private Button button1;
    private Button button2;
    private Button button3;
    private Button button4;
    private Button button5;
  }
}
