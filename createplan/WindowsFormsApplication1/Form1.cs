using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {
           
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*System.Drawing.SolidBrush myBrush = new System.Drawing.SolidBrush(System.Drawing.Color.Yellow);
            System.Drawing.Graphics formGraphics;
            formGraphics = this.CreateGraphics();
            formGraphics.FillRectangle(myBrush, new Rectangle(0, 0, 400, 400));
            myBrush.Dispose();
            formGraphics.Dispose();
            */

            string s1 = textBox1.Text;
            int[] genome = s1.Split(',').Select(n => Convert.ToInt32(n)).ToArray();

            int i;
            int len = genome.Length;
            int scale = Convert.ToInt32(400 / 80);
            for (i=0; i <= len; i+=4)
            {
                int width =scale*(genome[i]-genome[i+2]);
                int hight = scale*(genome[i + 1] - genome[i + 3]);
                int a = scale*(genome[i] - width);
                int b = scale* genome[i + 1];
               // int c = genome[i + 2] + width;
               // int d = genome[i + 3];

                System.Drawing.SolidBrush myBrush = new System.Drawing.SolidBrush(System.Drawing.Color.Blue);
                System.Drawing.Graphics formGraphics;
                formGraphics = this.CreateGraphics();
                formGraphics.FillRectangle(myBrush, new Rectangle(a, b, width, hight));
                myBrush.Dispose();
                formGraphics.Dispose();
            }



        }
    }
}
