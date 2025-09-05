namespace Calculator
{
  public partial class Calculator : Form
  {
    public Calculator()
    {
      InitializeComponent();

      KeyDown += Calculator_KeyDown;
    }

    private void button1_Click(object sender, EventArgs e)
    {
      label1.Text = ((Button)sender).Text;
    }

    private void button2_Click(object sender, EventArgs e)
    {
      label1.Text = ((Button)sender).Text;
    }

    private void button3_Click(object sender, EventArgs e)
    {
      label1.Text = ((Button)sender).Text;
    }

    private void button4_Click(object sender, EventArgs e)
    {
      label1.Text = ((Button)sender).Text;
    }

    private void button5_Click(object sender, EventArgs e)
    {
      Calculate();
    }

    private void Calculate()
    {

      if (textBox1.Text.Contains(','))
      {
        textBox1.Text = textBox1.Text.Replace(',', '.');
      }
      else if (textBox2.Text.Contains(','))
      {
        textBox2.Text = textBox2.Text.Replace(',', '.');
      }

      double x1, x2, x;

      // Проверка для конвертации значений из textBox1 и textBox2
      if (!double.TryParse(textBox1.Text, out x1) || !double.TryParse(textBox2.Text, out x2))
      {
        label2.Text = "= ERROR!";
        return;
      }

      // Проверка, что в label1 есть хотя бы 1 символ
      if (string.IsNullOrEmpty(label1.Text))
      {
        label2.Text = "= ERROR!";
        return;
      }

      // Выполнение операции в зависимости от знака в label1
      switch (label1.Text[0])
      {
        case '+':
          x = x1 + x2;
          break;
        case '-':
          x = x1 - x2;
          break;
        case '/':
          if (x2 == 0)
          {
            label2.Text = "= ERROR!";
            return;
          }
          x = x1 / x2;
          break;
        case '*':
          x = x1 * x2;
          break;
        default:
          label2.Text = "= ERROR!";
          return;
      }
      // Запись результата в label2
      label2.Text = "= " + x;
    }

    private void Calculator_KeyDown(object sender, KeyEventArgs e)
    {
      switch (e.KeyCode)
      {
        case Keys.Add:
        case Keys.Oemplus:  // Обработка нажатия клавиши "+" на основной клавиатуре
          label1.Text = "+"; // Предотвращение ввода текста в TextBox
          e.Handled = true;  // Подавление дальнейшей обработки клавиши
          e.SuppressKeyPress = true;
          break;

        case Keys.Subtract:
        case Keys.OemMinus: // Обработка нажатия клавиши "-" на основной клавиатуре
          label1.Text = "-";
          e.Handled = true;
          e.SuppressKeyPress = true;
          break;

        case Keys.D8 when e.Shift: // Обработка нажатия клавиши "*" на основной клавиатуре
        case Keys.Oem8:     
          label1.Text = "*";
          e.Handled = true;
          e.SuppressKeyPress = true;
          break;

        case Keys.Divide:
        case Keys.OemQuestion: // Некоторые клавиатуры используют "/" на основной клавиатуре
          label1.Text = "/";
          e.Handled = true;
          e.SuppressKeyPress = true;
          break;

        case Keys.Enter: // Обработка нажатия клавиши "Enter" на основной и цифровой клавиатуре
          Calculate();
          e.Handled = true;
          e.SuppressKeyPress = true;
          break;
      }
    }
  }
}