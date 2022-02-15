using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Graph
{
    public partial class Frm : Form
    {
        double f(double x, double a, double b, double c, double d)
        {

            double y = Math.Abs(Math.Abs(Math.Abs(a * x * x + b* x) - c) - d);
            return y;
        }
        public Frm()
        {
            InitializeComponent();
        }

        private void pnl_Paint(object sender, PaintEventArgs e)
        {
            var psk = e.Graphics;

            //Рисуем систему координат
            using (Pen pen = new Pen(Color.Aqua, 2))
            {

                Font my_font = new Font("Mistral", 14, FontStyle.Bold);
                Font my_font_numb = new Font("Mistral", 8, FontStyle.Bold);
                int pnl_weight = 600;
                //Рисуем ось
                for (int i = 0; i <= pnl_weight; i += 20)
                {
                    psk.DrawLine(new Pen(Color.LightSlateGray, 1), 0, i, pnl_weight, i);
                    psk.DrawLine(new Pen(Color.LightSlateGray, 1), i, 0, i, pnl_weight);

                }
                psk.DrawLine(new Pen(Color.LightSlateGray, 1), 599, 0, 599, 599);
                psk.DrawLine(new Pen(Color.LightSlateGray, 1), 0, 599, 599, 599);
                //Рисуем штриховку
                for (int i = 20; i <= pnl_weight; i += 20)
                {
                    psk.DrawLine(new Pen(Color.Black, 1), (pnl_weight / 2) - 5, i, (pnl_weight / 2) + 5, i);
                    psk.DrawLine(new Pen(Color.Black, 1), i, (pnl_weight / 2) - 5, i, (pnl_weight / 2) + 5);
                }
                //Нумеруем
                int k1, k2, k3, k4;
                k1 = -1;
                k2 = 1;
                k3 = 1;
                k4 = -1;
                for (int i = pnl_weight / 2 + 20; i < pnl_weight; i += 20)
                {
                    psk.DrawString("/4", my_font_numb, Brushes.Black, (pnl_weight / 2) + 25, i - 10);
                    k1--;
                    psk.DrawString(k1.ToString(), my_font_numb, Brushes.Black, (pnl_weight / 2) + 10, i - 10);
                    k1--;

                }

                for (int i = pnl_weight / 2 + 20; i < pnl_weight; i += 20)
                {
                    psk.DrawString("4", my_font_numb, Brushes.Black, i - 5, (pnl_weight / 2) - 13);
                    psk.DrawString("--", my_font_numb, Brushes.Black, i - 5, (pnl_weight / 2) - 18);
                    k2++;
                    psk.DrawString(k2.ToString(), my_font_numb, Brushes.Black, i - 5, (pnl_weight / 2) - 23);
                    k2++;
                }


                for (int i = pnl_weight / 2; i > 20; i -= 20)
                {
                    psk.DrawString("4", my_font_numb, Brushes.Black, i - 25, (pnl_weight / 2) + 23);
                    psk.DrawString("--", my_font_numb, Brushes.Black, i - 25, (pnl_weight / 2) + 16);
                    k4--;
                    psk.DrawString(k4.ToString(), my_font_numb, Brushes.Black, i - 30, (pnl_weight / 2) + 10);
                    k4--;
                }

                for (int i = pnl_weight / 2; i > 20; i -= 20)
                {
                    psk.DrawString("/4", my_font_numb, Brushes.Black, (pnl_weight / 2) - 20, i - 30);
                    k3++;
                    psk.DrawString(k3.ToString(), my_font_numb, Brushes.Black, (pnl_weight / 2) - 30, i - 30);
                    k3++;
                }
                // Рисуем ось абсцисс и ординат
                psk.DrawLine(new Pen(Color.Gray, 2), pnl_weight, pnl_weight / 2, 0, pnl_weight / 2);
                psk.DrawLine(new Pen(Color.Gray, 2), pnl_weight / 2, pnl_weight, pnl_weight / 2, 0);

                //Подписываем оси и ставим стрелки
                Pen blackPen = new Pen(Color.Black, 1);
                PointF point1 = new PointF(590, 295);
                PointF point2 = new PointF(600, 300);
                PointF point3 = new PointF(590, 305);
                PointF[] curvePoints =
                {
                    point1,
                    point2,
                    point3,
                };

                psk.DrawPolygon(new Pen(Color.Gray, 2), curvePoints);


                PointF point4 = new PointF(295, 10);
                PointF point5 = new PointF(300, 0);
                PointF point6 = new PointF(305, 10);
                PointF[] curvePointss =
                 {
                     point4,
                     point5,
                     point6,
                 };
                psk.DrawPolygon(new Pen(Color.Gray, 2), curvePointss);



                psk.DrawString("X", my_font, Brushes.Red, 585, 310);
                psk.DrawString("Y", my_font, Brushes.Red, 310, 0);
            }

        }



        void btn_Click(object sender, EventArgs e)
        {
            //Строим график
            int pnl_weight = 600;
            Bitmap pen = new Bitmap(1, 1);
            pen.SetPixel(0, 0, Color.Black);
            double a = Convert.ToDouble(per_a.Text);
            double b = Convert.ToDouble(per_b.Text);
            double c = Convert.ToDouble(per_c.Text);
            double d = Convert.ToDouble(per_d.Text);
            double x, y, xp = -10, yp = f(xp, a, b, c, d), i;
            // double x_max=5, x_min=-5;
            System.Drawing.Graphics g = pnl.CreateGraphics();
            for (i = -15; i <= 14; i += 0.001D)
            {
                x = i;
                y = f(x, a, b, c, d) * 2;
                g.DrawLine(new Pen(Color.Black, 2), Convert.ToInt32((xp * 40 + pnl_weight / 2)), Convert.ToInt32(pnl_weight / 2 - yp * 20), Convert.ToInt32((x * 40 + pnl_weight / 2)), Convert.ToInt32(pnl_weight / 2 - y * 20));
                xp = x;
                yp = y;
            }
        }

        private void clr_Click(object sender, EventArgs e)
        {
            var psk = pnl.CreateGraphics();
            psk.Clear(Color.Moccasin);
            //Рисуем систему координат
            using (Pen pen = new Pen(Color.Aqua, 2))
            {

                Font my_font = new Font("Mistral", 14, FontStyle.Bold);
                Font my_font_numb = new Font("Mistral", 8, FontStyle.Bold);
                int pnl_weight = 600;
                //Рисуем ось
                for (int i = 0; i <= pnl_weight; i += 20)
                {
                    psk.DrawLine(new Pen(Color.LightSlateGray, 1), 0, i, pnl_weight, i);
                    psk.DrawLine(new Pen(Color.LightSlateGray, 1), i, 0, i, pnl_weight);

                }
                psk.DrawLine(new Pen(Color.LightSlateGray, 1), 599, 0, 599, 599);
                psk.DrawLine(new Pen(Color.LightSlateGray, 1), 0, 599, 599, 599);
                //Рисуем штриховку
                for (int i = 20; i <= pnl_weight; i += 20)
                {
                    psk.DrawLine(new Pen(Color.Black, 1), (pnl_weight / 2) - 5, i, (pnl_weight / 2) + 5, i);
                    psk.DrawLine(new Pen(Color.Black, 1), i, (pnl_weight / 2) - 5, i, (pnl_weight / 2) + 5);
                }
                //Нумеруем
                int k1, k2, k3, k4;
                k1 = -1;
                k2 = 1;
                k3 = 1;
                k4 = -1;
                for (int i = pnl_weight / 2 + 20; i < pnl_weight; i += 20)
                {
                    psk.DrawString("/4", my_font_numb, Brushes.Black, (pnl_weight / 2) + 25, i - 10);
                    k1--;
                    psk.DrawString(k1.ToString(), my_font_numb, Brushes.Black, (pnl_weight / 2) + 10, i - 10);
                    k1--;

                }

                for (int i = pnl_weight / 2 + 20; i < pnl_weight; i += 20)
                {
                    psk.DrawString("4", my_font_numb, Brushes.Black, i - 5, (pnl_weight / 2) - 13);
                    psk.DrawString("--", my_font_numb, Brushes.Black, i - 5, (pnl_weight / 2) - 18);
                    k2++;
                    psk.DrawString(k2.ToString(), my_font_numb, Brushes.Black, i - 5, (pnl_weight / 2) - 23);
                    k2++;
                }


                for (int i = pnl_weight / 2; i > 20; i -= 20)
                {
                    psk.DrawString("4", my_font_numb, Brushes.Black, i - 25, (pnl_weight / 2) + 23);
                    psk.DrawString("--", my_font_numb, Brushes.Black, i - 25, (pnl_weight / 2) + 16);
                    k4--;
                    psk.DrawString(k4.ToString(), my_font_numb, Brushes.Black, i - 30, (pnl_weight / 2) + 10);
                    k4--;
                }

                for (int i = pnl_weight / 2; i > 20; i -= 20)
                {
                    psk.DrawString("/4", my_font_numb, Brushes.Black, (pnl_weight / 2) - 20, i - 30);
                    k3++;
                    psk.DrawString(k3.ToString(), my_font_numb, Brushes.Black, (pnl_weight / 2) - 30, i - 30);
                    k3++;
                }
                // Рисуем ось абсцисс и ординат
                psk.DrawLine(new Pen(Color.Gray, 2), pnl_weight, pnl_weight / 2, 0, pnl_weight / 2);
                psk.DrawLine(new Pen(Color.Gray, 2), pnl_weight / 2, pnl_weight, pnl_weight / 2, 0);

                //Подписываем оси и ставим стрелки
                Pen blackPen = new Pen(Color.Black, 1);
                PointF point1 = new PointF(590, 295);
                PointF point2 = new PointF(600, 300);
                PointF point3 = new PointF(590, 305);
                PointF[] curvePoints =
                {
                    point1,
                    point2,
                    point3,
                };

                psk.DrawPolygon(new Pen(Color.Gray, 2), curvePoints);


                PointF point4 = new PointF(295, 10);
                PointF point5 = new PointF(300, 0);
                PointF point6 = new PointF(305, 10);
                PointF[] curvePointss =
                 {
                     point4,
                     point5,
                     point6,
                 };
                psk.DrawPolygon(new Pen(Color.Gray, 2), curvePointss);



                psk.DrawString("X", my_font, Brushes.Red, 585, 310);
                psk.DrawString("Y", my_font, Brushes.Red, 310, 0);
            }
        }
    }
}
