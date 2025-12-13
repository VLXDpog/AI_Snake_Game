
                # Kiểm tra nút bấm
                for btn in self.buttons:
                    if btn.is_clicked(event):
                        return btn.action_id # Trả về '1', '2', '3' hoặc '4'

            # Vẽ các nút
            for btn in self.buttons:
                btn.draw(self.screen)


            pygame.display.flip()
